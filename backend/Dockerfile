FROM python:3.9-slim

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# Копируем код
COPY . .

# Собираем статику (важно: после копирования кода!)
RUN python manage.py collectstatic --noinput

# Запускаем с ПРАВИЛЬНЫМ именем модуля
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]