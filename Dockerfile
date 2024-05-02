FROM python:3.10

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY req.txt .

RUN pip install -r req.txt

COPY . .