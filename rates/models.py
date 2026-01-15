# models.py
from django.db import models

class CurrencyRate(models.Model):
    # Код валюты, например 'USD', 'EUR', 'RUB', 'KZT'
    code = models.CharField(max_length=3)
    
    # Курс (например, 3.22 BYN за 1 USD)
    rate = models.DecimalField(max_digits=18, decimal_places=6)
    
    # Базовая валюта (теперь BYN)
    base_currency = models.CharField(max_length=3, default='BYN')
    
    # Источник данных
    source = models.CharField(max_length=50, default='exchangerate-api')
    
    # Время фиксации курса
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"1 {self.code} = {self.rate:.4f} {self.base_currency}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'