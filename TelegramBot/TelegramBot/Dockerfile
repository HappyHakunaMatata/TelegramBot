# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.11.5-slim
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y libpq-dev gcc tzdata
RUN pip3 install psycopg2-binary

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /TelegramBot
COPY requirements.txt /TelegramBot
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /TelegramBot
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runbot"]

