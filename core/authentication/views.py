from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View


class Login(View):
	def get(self, *args, **kwargs):
		return render(self.request, "login.html")

	def post(self, *args, **kwargs):
		email = self.request.POST["email"]
		password = self.request.POST["password"]

		user = authenticate(self.request, username=email, password=password)

		if user is not None:
			login(self.request, user)
			return redirect("home")

		messages.success(self.request, "Erro: Email ou senha inválido")
		return redirect("login")


class Logout(View):
	def post(self, *args, **kwargs):
		logout(self.request)
		return redirect("login")
