import os
from celery import Celery


# Указываем Celery, где искать настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Загружаем настройки из файла settings.py, используя префикс CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')


# Автоматически находим задачи (tasks.py) во всех приложениях
app.autodiscover_tasks()