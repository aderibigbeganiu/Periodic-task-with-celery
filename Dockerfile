FROM python:3.9.6-alpine
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip setuptools wheel

WORKDIR /usr/src/celery-tut

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY requirements.txt /usr/src/celery-tut/
RUN pip install -r requirements.txt
COPY . /usr/src/celery-tut/

RUN python manage.py makemigrations
# RUN python manage.py migrate


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "celery_tut.wsgi:application"]