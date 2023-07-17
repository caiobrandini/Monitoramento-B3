from django.shortcuts import render, redirect
from monitoring.models import StockListener, Stock
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from django.views import View

class CreateStockListener(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        return render(self.request, 'createStockListener.html')

    def post(self, *arsg, **kwargs):
        
        form_errors = []

        try:
            stock = Stock.objects.get(code= self.request.POST['stock_name'])
        except ObjectDoesNotExist:
            form_errors.append('A seleção do ativo possui formatação incorreta')

        try:
            frequency = int(self.request.POST['frequency'])
        except:
            form_errors.append('O campo de frequência possui formatação incorreta')

        try:
            upper_limit = float(self.request.POST['upper_limit'].replace(',','.'))
        except:
            form_errors.append('O campo de limite superior possui formatação incorreta')
        
        try:
            inferior_limit = float(self.request.POST['inferior_limit'].replace(',','.'))
        except:
            form_errors.append('O campo de limite inferior possui formatação incorreta')
        
        if form_errors:
            return render(self.request, 'createStockListener.html', {'errors': form_errors})

        StockListener.objects.create(
            user = self.request.user,
            stock = stock,
            frequency = frequency,
            upper_tunnel_limit = upper_limit,
            inferior_tunnel_limit = inferior_limit,
        )

        return redirect('home')