from authentication.views import Login, Logout
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
	path("login/", Login.as_view(), name="login"),
	path("logout", Logout.as_view(), name="logout"),
	path("sign-up/", TemplateView.as_view(template_name="sign-up.html"), name="sign-up"),
]
