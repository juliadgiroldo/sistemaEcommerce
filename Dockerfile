FROM python:3.11.3-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN cat requirements.txt  # Log das informações do requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000'] 