from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_tut.settings")

app = Celery(
    'celery_tut',
    backend="redis://redis:6379/0",
    broker="redis://redis:6379/0"
)

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()
