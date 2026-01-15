from django.urls import path
from .views import CurrencyRateListView, RateChartView

urlpatterns = [
    path('rates/', CurrencyRateListView.as_view(), name='rates_list'),
    path('chart/', RateChartView.as_view(), name='rate_chart'),
   
]