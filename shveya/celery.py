import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'shveya.settings'
)

app = Celery('shveya')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

