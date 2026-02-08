FROM python:3.9-slim

WORKDIR /app

# Сначала копируем только requirements для кэширования
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# Копируем весь код
COPY . .

# Собираем статику.
RUN python manage.py collectstatic --noinput

# Запускаем gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "taski_backend.wsgi"]