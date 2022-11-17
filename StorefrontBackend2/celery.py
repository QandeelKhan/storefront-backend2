import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'StorefrontBackend2.settings.dev')

# any name to initialize a celery instance i.e Celery('abc')
celery = Celery('StorefrontBackend2')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
