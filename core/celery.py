# yourproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# create a Celery instance and configure it using the settings from Django
celery_app = Celery('core')

# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
celery_app.autodiscover_tasks()


celery_app.conf.beat_schedule = {
    'send-crypto-quote-every-minute': {
        'task': 'crypto.tasks.send_crypto_quote',
        'schedule': crontab(minute='*'),
    },
}