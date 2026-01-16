#

# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rates.views import RateChartView, update_rates_api  # импортируем view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rates.urls')),
    
    # Добавляем отдельные пути для корня
    path('', RateChartView.as_view(), name='home'),  # корень показывает график
    path('rates/', include('rates.urls')),  # всё из rates доступно по /rates/
    path('api/update-rates/', update_rates_api, name='update_rates'), #для рендер
]