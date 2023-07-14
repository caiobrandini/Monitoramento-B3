from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class HomeView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		return render(self.request, "home.html",)
