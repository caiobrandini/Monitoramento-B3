from monitoring.views import CreateStockListener
from django.urls import path

urlpatterns = [
	path("create/", CreateStockListener.as_view(), name="create_stock_listener"),
]