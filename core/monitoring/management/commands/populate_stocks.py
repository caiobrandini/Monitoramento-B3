import MetaTrader5 as mt5
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from monitoring.models import Stock


class Command(BaseCommand):
	help = "Use Meta Trader 5 to populate stocks"

	def handle(self, *args, **kwargs):

		if not mt5.initialize():
			raise Exception("md5 initialize failed, error code: ", mt5.last_error())

		stocks = mt5.symbols_get()

		stock_to_create = []
		for stock in stocks:
			new_stock = Stock(name=stock.name)
			stock_to_create.append(new_stock)

		with atomic():
			Stock.objects.bulk_create(stock_to_create)

		mt5.shutdown()
