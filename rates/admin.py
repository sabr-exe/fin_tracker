from django.contrib import admin
from .models import CurrencyRate

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    # Список полей, которые будут видны в таблице
    list_display = ('code', 'rate', 'base_currency', 'created_at')
    # Добавляем фильтрацию по валюте и дате
    list_filter = ('code', 'created_at')
    # Поиск по коду валюты
    search_fields = ('code',)