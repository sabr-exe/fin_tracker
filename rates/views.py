import json
from rest_framework.generics import ListAPIView
from .models import CurrencyRate
from .serializers import CurrencyRateSerializer
from django.shortcuts import render
from django.views import View



class CurrencyRateListView(ListAPIView):
    queryset = CurrencyRate.objects.all().order_by('-created_at')
    serializer_class = CurrencyRateSerializer


# views.py (упрощенная версия без API)
import json
from datetime import timedelta
from django.views import View
from django.shortcuts import render
from django.db.models import Avg, Max, Min
from django.utils import timezone
from .models import CurrencyRate

class RateChartView(View):
    def get(self, request, currency='USD'):
        currency = request.GET.get('currency', currency).upper()
        
        valid_currencies = ['USD', 'EUR', 'RUB', 'KZT', 'PLN', 'BYN']
        
        if currency not in valid_currencies:
            currency = 'USD'
        
        # Получаем последние 30 записей для выбранной валюты
        rates = CurrencyRate.objects.filter(
            code=currency.upper()
        ).order_by('-created_at')[:30]
        
        # Переворачиваем для правильного порядка (от старых к новым)
        rates = list(reversed(rates))
        
        # Подготавливаем данные для графика
        labels = [r.created_at.strftime("%d.%m %H:%M") for r in rates]
        values = [float(r.rate) for r in rates]
        
        # Текущий курс
        current_rate = float(rates[-1].rate) if rates else 0
        
        # Данные для всех валют
        currencies_data = []
        currency_names = {
            'USD': 'Доллар США',
            'EUR': 'Евро', 
            'RUB': 'Российский рубль',
            'KZT': 'Казахстанский тенге',
            'PLN': 'Польский злотый',
            'BYN': 'Белорусский рубль',
        }
        
        for curr_code in valid_currencies:
            last_rate = CurrencyRate.objects.filter(
                code=curr_code
            ).order_by('-created_at').first()
            
            if last_rate:
                currencies_data.append({
                    'code': curr_code,
                    'name': currency_names.get(curr_code, curr_code),
                    'rate': float(last_rate.rate)
                })
        
        context = {
            'labels_json': json.dumps(labels),
            'values_json': json.dumps(values),
            'selected_currency': currency,
            'current_rate': current_rate,
            'currencies_data': currencies_data,
            'base_currency': 'BYN',
            'update_time': timezone.now().strftime("%H:%M"),
            'current_date': timezone.now().strftime("%d.%m.%Y"),
            'current_year': timezone.now().year,
        }
        
        return render(request, 'rates/chart.html', context)