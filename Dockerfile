FROM python:3.10-slim

WORKDIR /app

# Zaruriy tizim kutubxonalari
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Railway uchun port
ENV PORT=8080
EXPOSE 8080

# Django-ni ishga tushirish
CMD gunicorn Boshliq.wsgi:application --bind 0.0.0.0:$PORT