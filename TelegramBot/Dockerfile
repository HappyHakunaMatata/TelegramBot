# syntax=docker/dockerfile:1.4
#python:3.11.5
FROM --platform=$BUILDPLATFORM python:3.11.5-slim
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y libpq-dev gcc tzdata
RUN pip3 install psycopg2-binary

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 17620
WORKDIR /TelegramBot 
COPY requirements.txt /TelegramBot
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip install gunicorn
COPY . /TelegramBot
#RUN python manage.py collectstatic --no-input

CMD ["gunicorn","--bind", "0.0.0.0:17620", "TelegramBot.wsgi:application"]

