from datetime import datetime
from time import sleep

import MetaTrader5 as mt5
from django.core.management.base import BaseCommand
from monitoring.models import StockListener, StockRecord
from pytz import timezone

from core.helpers.sendmail import sendmail


class Command(BaseCommand):
	help = "Update stock values every minute"

	def handle(self, *args, **kwargs):
		def send_action_email(user, action, stock_name):
			mail_subject = f"{action.upper()} - Monitoramento B3"
			mail_body = f"""
				O ativo ultrapassou o limete estabelecido no seu monitoramento do ativo {stock_name}
			"""

			sendmail(user.email, mail_subject, mail_body)

		def update_stock_values():
			now = datetime.now()
			tz = timezone("America/Sao_Paulo")
			now_with_tz = now.astimezone(tz)
			stock_listeners = StockListener.objects.all()

			if not mt5.initialize():
				raise Exception("md5 initialize failed, error code: ", mt5.last_error())

			stock_records_to_create = []
			for stock_listener in stock_listeners:
				last_record = stock_listener.stockrecord_set.order_by("-datetime").first()
				last_update = last_record.datetime if last_record else None

				if last_update:
					last_update_timedelta_seconds = (now_with_tz - last_update).seconds
					last_update_timedelta_minutes = int(last_update_timedelta_seconds / 60)

				if last_update is None or stock_listener.frequency <= last_update_timedelta_minutes:
					stock_name = stock_listener.stock.name
					mt5.symbol_select(stock_name)
					stock_info = mt5.symbol_info_tick(stock_name)

					if stock_info:
						stock_value = stock_info.last
						new_stock_record = StockRecord(
							datetime=now_with_tz, value=stock_value, stock_listener=stock_listener
						)
						stock_records_to_create.append(new_stock_record)

						if stock_value < stock_listener.inferior_tunnel_limit:
							send_action_email(stock_listener.user, "COMPRAR", stock_name)

						elif stock_value > stock_listener.upper_tunnel_limit:
							send_action_email(stock_listener.user, "VENDER", stock_name)

			StockRecord.objects.bulk_create(stock_records_to_create)
			for created_stock in stock_records_to_create:
				print(
					f"NEW STOCKRECORD: {created_stock.datetime}, {created_stock.value}, {created_stock.stock_listener}"
				)

		def continuously_monitor():
			while True:
				update_stock_values()
				sleep(60)

		continuously_monitor()
