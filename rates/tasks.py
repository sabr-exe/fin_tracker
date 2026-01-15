import requests
from celery import shared_task
from django.utils import timezone
from decimal import Decimal
from .models import CurrencyRate


@shared_task(name='rates.tasks.fetch_currency_rates')
def fetch_currency_rates():
    url = "https://open.er-api.com/v6/latest/BYN"  # ← Меняем KZT на BYN
    response = requests.get(url)
    data = response.json()

    if data.get('result') == 'success':
        rates = data.get('rates', {})
        
        # Сохраняем несколько валют
        currencies = ['USD', 'EUR', 'RUB', 'KZT', 'PLN']
        
        for currency_code in currencies:
            if currency_code in rates:
                rate = rates[currency_code]
                if float(rate) != 0:
                    # API: 1 BYN = X [валюта], нужно: 1 [валюта] = 1/X BYN
                    final_rate = 1 / float(rate)
                    
                    CurrencyRate.objects.create(
                        code=currency_code,
                        rate=Decimal(str(final_rate)),
                        base_currency='BYN',  # ← Меняем на BYN
                        source='exchangerate-api',
                        created_at=timezone.now()
                    )
        
        return f"Updated {len(currencies)} rates to BYN"
    return "Failed to update rates"