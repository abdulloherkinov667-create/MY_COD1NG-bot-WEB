# Deployment Checklist - Railway.app

## ✅ O'tkazilgan Xatolarni Bartaraf Qilish

### 1. **Settings Configuration** (`Boshliq/settings.py`)
- ✅ Environment variables'dan `SECRET_KEY` o'qiladi
- ✅ Environment variables'dan `DEBUG` o'qiladi
- ✅ Environment variables'dan `ALLOWED_HOSTS` o'qiladi
- ✅ `STATIC_ROOT` qo'shildi (`staticfiles/`)
- ✅ Logging configuration qo'shildi (console + detailed)
- ✅ Security headers qo'shildi (`SECURE_PROXY_SSL_HEADER`, `SECURE_SSL_REDIRECT`)
- ✅ Middleware o'rganizatsiyasi to'g'rilandi

### 2. **Health Check Endpoint** (`app/views.py` + `Boshliq/urls.py`)
- ✅ `/health/` endpoint qo'shildi
- ✅ Railway ilovani monitoring qilishi uchun JSON response qaytaradi

### 3. **Dockerfile Optimization**
- ✅ Static files collection qo'shildi (`collectstatic`)
- ✅ Health check qo'shildi (30s intervals)
- ✅ Timeout orttildi (`--timeout 120`)
- ✅ `curl` utility qo'shildi (health check uchun)
- ✅ Detailed logging enabled

### 4. **Documentation**
- ✅ `RAILWAY_SETUP.md` yaratildi (deployment ko'rsatmalari)
- ✅ `.env.example` yaratildi (environment variables shablon)

---

## 🚀 Railway'da Deploy Qilish Uchun Talab Qilingan Qadamlar

### Step 1: Railway.app Account Yaratish
```
https://railway.app/account
```

### Step 2: New Project Yaratish
- "Create a new project" → "GitHub" → Repository tanlang
- Yoki "Deploy from GitHub" → Bu repo'ni connect qiling

### Step 3: Environment Variables Soslamasi
Railway Dashboard → Variables bo'limiga quyidagi'ni kiriting:

**Zarur (MUST):**
```
SECRET_KEY=<generate-strong-random-key>
DEBUG=False
```

**Recommended:**
```
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
```

### Step 4: Deploy
Railway avtomatik ravishda:
1. ✅ Dockerfile topadi
2. ✅ Docker image build qiladi
3. ✅ Container ishga tushiradi
4. ✅ Migration ishlatadi
5. ✅ Health check monitoringi boshlaydi

### Step 5: Logs'ni Tekshirish
Agar muammo bo'lsa:
```
Railway Dashboard → Logs tab → Scroll down xatoni ko'ring
```

---

## 🔍 Possible Xatolar va Yechimlar

### Error: "Application failed to respond"
**Tekshiring:**
- [ ] Logs'da qanday xato chiqayotganini ko'rding?
- [ ] `http://yourdomain.com/health/` javob bermoqda?
- [ ] SECRET_KEY va DEBUG environment variables set qilingan?

### Error: "ModuleNotFoundError"
**Yechim:**
```bash
# requirements.txt'da hamma kutubxona bor:
cat requirements.txt
```

### Error: "TemplateDoesNotExist: error.html"
**Yechim:**
- `templates/` papkasi root'da bo'lishi kerak
- `error.html` faylining tori to'g'ri

### Error: "django.db.utils.OperationalError: no such table"
**Yechim:**
- Migration Dockerfile'da avtomatik ishlatyapti
- Agar ham muammo bo'lsa, Railway terminal'dan ishlatish:
```bash
railway run python manage.py migrate
```

---

## 📊 Health Check Test

Local'da test qilish:
```bash
# Terminal'dan
docker build -t boshliq .
docker run -p 8080:8080 \
  -e SECRET_KEY=test-key \
  -e DEBUG=False \
  boshliq

# Boshqa terminal'da
curl http://localhost:8080/health/
# Expected: {"status": "healthy", "service": "Boshliq"}

curl http://localhost:8080/
# Expected: error.html render qiladi
```

---

## 📝 Qo'shimcha Sozlamalar (Production'da)

### PostgreSQL Database (Recommended)
SQLite o'rniga PostgreSQL'ga o'ting:

1. Railway'da PostgreSQL add-on yaratish
2. `DATABASE_URL` environment variable'ni copy qilish
3. `requirements.txt'ga `psycopg2-binary` qo'shish
4. `settings.py'da database config'ni update qilish

### Static Files (CDN)
CSS/JS/Image'lar uchun:
1. AWS S3 yoki CloudFlare bo'lish mumkin
2. `django-storages` package qo'shish
3. AWS credentials set qilish

### SSL Certificate
- Railway avtomatik ravishda Let's Encrypt SSL beradi
- HTTPS avtomatik redirect qilinadi

---

## ✨ Completion Checklist

- [ ] `SECRET_KEY` strong random string
- [ ] `DEBUG=False` production'da
- [ ] `ALLOWED_HOSTS` correct domains
- [ ] Environment variables Railway'da set
- [ ] Docker build local'da ishla: `docker build -t boshliq .`
- [ ] Health check endpoint `/health/` javob beradi
- [ ] Logs'da xato yo'q
- [ ] Application `http://yourdomain.com` responsiv

---

## 📞 Emergency Restart

Agar application freeze bo'lsa:
```bash
railway redeploy
# yoki
railway run bash  # SSH into container
```

---

**Last Updated:** 2026-05-13
**Django Version:** 5.2.14
**Python Version:** 3.10
**Platform:** Railway.app
