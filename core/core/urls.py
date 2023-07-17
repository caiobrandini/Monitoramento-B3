from django.contrib import admin
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("admin/", admin.site.urls),
	path("auth/", include("authentication.urls"), name="auth"),
    path("monitoring/", include("monitoring.urls"), name="monitoring"),
]
