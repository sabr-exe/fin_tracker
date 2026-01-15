# config/__init__.py должен содержать:
from .celery import app as celery_app

__all__ = ('celery_app',)