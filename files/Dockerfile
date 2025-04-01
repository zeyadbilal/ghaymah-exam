# استخدم صورة Python الأساسية
FROM python:3.9

# تعيين دليل العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى الحاوية
COPY requirements.txt requirements.txt
COPY app.py app.py

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل التطبيق
CMD ["python", "app.py"]
