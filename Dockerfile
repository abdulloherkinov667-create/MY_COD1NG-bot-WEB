# 1. Python-ning barqaror va yengil versiyasi
FROM python:3.10-slim

# 2. Python muhiti uchun muhim sozlamalar
# .pyc fayllar yaratilishini to'xtatadi va loglarni terminalga tezroq chiqaradi
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# 3. Ishchi papkani yaratish
WORKDIR /app

# 4. Tizim kutubxonalarini o'rnatish
# apt-get keshini tozalash orqali image hajmini kichraytiramiz
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Pip-ni yangilash va kutubxonalarni o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Loyihani nusxalash
COPY . .

# 7. Portni ochish
EXPOSE 8080

# 8. Ishga tushirish buyrug'i (JSON formatida)
# Railway signallarini to'g'ri qabul qilishi uchun shunday yozish tavsiya etiladi
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py check --settings=Boshliq.settings && gunicorn Boshliq.wsgi:application --bind 0.0.0.0:${PORT} --workers 1 --log-level debug --access-logfile - --error-logfile -"]