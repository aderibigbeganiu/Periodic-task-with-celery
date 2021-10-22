from django.core.mail.message import EmailMessage
from celery_tut.celery import app
import sys
from django.conf import settings

from django.core.management import call_command


@app.task(name='bkup')
def bkup():
    sysout = sys.stdout
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', exclude=['contenttypes', 'auth'])
    sys.stdout = sysout
    email = EmailMessage(
        "backup", "backup from celery task",
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL, ]
    )
    email.attach_file('db.json')
    email.send()
