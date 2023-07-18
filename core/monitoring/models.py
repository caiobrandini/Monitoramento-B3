from django.contrib.auth.models import User
from django.db import models


class Stock(models.Model):
	name = models.CharField(max_length=100, unique=True)


class StockListenerManager(models.QuerySet):
	def filter_user_objects(self, user):
		return self.filter(user=user)


class StockListener(models.Model):
	objects = StockListenerManager.as_manager()

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	frequency = models.PositiveIntegerField()
	upper_tunnel_limit = models.DecimalField(max_digits=8, decimal_places=2)
	inferior_tunnel_limit = models.DecimalField(max_digits=8, decimal_places=2)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ["user", "stock"]


class StockRecord(models.Model):
	datetime = models.DateTimeField()
	value = models.DecimalField(max_digits=8, decimal_places=2)
	stock_listener = models.ForeignKey(StockListener, on_delete=models.CASCADE)

	class Meta:
		unique_together = ["stock_listener", "datetime"]
