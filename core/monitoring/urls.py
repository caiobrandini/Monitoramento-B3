from django.urls import path
from monitoring.views import CreateStockListener, DeleteStockListener

urlpatterns = [
	path("create/", CreateStockListener.as_view(), name="create_stock_listener"),
	path("delete/", DeleteStockListener.as_view(), name="delete_stock_listener"),
]
