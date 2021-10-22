from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery_tut.celery import app


@app.task(name="add")
def add(x, y):
    return x + y
