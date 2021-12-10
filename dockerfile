FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install --upgrade pip

# Psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "server.py"]