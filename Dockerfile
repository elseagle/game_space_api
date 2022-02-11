# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt-get update && apt-get install
RUN apt-get install -y libpq-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt

COPY . .
# CMD ["gunicorn", "--bind", "0.0.0.0:6000", "app:app"]
CMD [ "python3", "app.py"]
