FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install django-tastypie
RUN pip install djangorestframework
RUN pip install haversine
COPY . /code/
