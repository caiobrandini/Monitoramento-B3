from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from monitoring.models import StockListener


class HomeView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):

		user = self.request.user
		stock_listeners_objects = StockListener.objects.filter_user_objects(user)

		stock_listeners = []
		for stock_listener in stock_listeners_objects:

			stock_record_objects = stock_listener.stockrecord_set.all()

			graph_values = []
			graph_labels = []
			for stock_record in stock_record_objects:
				formated_datetime = stock_record.datetime.strftime("%d/%m/%y %H:%M")
				graph_labels.append(formated_datetime)
				graph_values.append(stock_record.value)

			stock_listeners.append(
				{
					"stock_code": stock_listener.stock.code,
					"frequency": stock_listener.frequency,
					"upper_tunnel_limit": stock_listener.upper_tunnel_limit,
					"inferior_tunnel_limit": stock_listener.inferior_tunnel_limit,
					"graph": {"labels": graph_labels, "values": graph_values},
				}
			)

		context = {"stock_listeners": stock_listeners, "username": self.request.user.username}

		return render(self.request, "home.html", context)
