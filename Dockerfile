FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /djangoproject2
COPY ./djangoproject2 /djangoproject2
WORKDIR /djangoproject2
