# Railway.app Deployment Guide

## Railway Dashboard'da quyidagilarni qiling:

### 1. Environment Variables'ni Set Qiling

Railway project → Settings → Variables bo'limiga quyidagi environment variables'ni kiriting:

```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
```

### 2. Build Command (Opsional, agar aniqlanmagan bo'lsa)
Railway avtomatik ravishda Dockerfile'ni topadi va ishga tushiradi.

### 3. Start Command (Opsional)
```
sh -c "python manage.py migrate --noinput && python manage.py check && exec gunicorn Boshliq.wsgi:application --bind 0.0.0.0:${PORT} --workers 1"
```

### 4. Port Configuration
Railway avtomatik ravishda $PORT environment variable'ni beradi (default 8080).
Dockerfile va Gunicorn command'da ${PORT} ishlatiladi - bu to'g'ri.

### 5. Health Check
Application endi `/health/` endpoint'ga javob beradi.
Railway ilovaning sog'lom ekanligini aniq bilib turadi.

## Xatolarni Ko'rish

Railway Dashboard → Logs bo'limida real-time logs ko'rasiz.
Agar "Application failed to respond" xatosi qolsa:

1. **Port xatosi**: "bind: address already in use" - bu Dockerfile'da PORT=8080 deb belgilangani shuni bildiradi
2. **Import xatosi**: "ModuleNotFoundError" - requirements.txt'da kutubxona yo'q
3. **Database xatosi**: "no such table" - migration ishlamagan
4. **Template xatosi**: "TemplateDoesNotExist" - templates/ papkasi to'g'ri joylashgan emas

## Local Teshlash

```bash
# Build Docker image
docker build -t boshliq .

# Ishga tushirish
docker run -p 8080:8080 \
  -e SECRET_KEY=test-secret-key \
  -e DEBUG=True \
  -e ALLOWED_HOSTS=localhost \
  boshliq

# Health check
curl http://localhost:8080/health/
# Javob: {"status": "healthy", "service": "Boshliq"}
```

## Common Muammolar va Yechimlar

| Muammo | Yechimi |
|--------|--------|
| "Application failed to respond" | Logs'ni oching, health check endpoint ishlamoqda |
| SQLite lock error | PostgreSQL'ga o'ting (production uchun tafsiya) |
| Static files yo'q | `collectstatic` Dockerfile'da bajaryladi |
| 502 Bad Gateway | Gunicorn worker'lar kashing bo'ydi, workers sonini oshiring |
| Timeout errors | `--timeout 120` Dockerfile'da set qilindi |

## Qo'shimcha Fayllar

- **requirements.txt** - Barcha Python kutubxonalari
- **Dockerfile** - Docker image konfiguratsiyasi
- **Boshliq/settings.py** - Django sozlamalari (environment variables'dan o'qiydi)
- **app/views.py** - Health check endpoint qo'shildi
- **Boshliq/urls.py** - Health check URL'i qo'shildi
