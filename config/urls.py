#

# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rates.views import RateChartView # импортируем view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rates.urls')),
    
    # Добавляем отдельные пути для корня
    path('', RateChartView.as_view(), name='home'),  # корень показывает график
    path('rates/', include('rates.urls')),  # всё из rates доступно по /rates/

]