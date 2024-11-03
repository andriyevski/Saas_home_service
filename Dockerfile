# Використовуємо Python 3.12
FROM python:3.12-slim-bullseye

# Встановлення залежностей системи
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Налаштування робочого каталогу
WORKDIR /code

# Копіюємо файли проекту
COPY requirements.txt /tmp/requirements.txt
COPY ./src /code

# Встановлення Python залежностей
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

    #!/bin/bash
RUN_PORT="${PORT:-8000}"

python manage.py migrate --no-input
gunicorn ${PROJ_NAME}.wsgi:application --bind "0.0.0.0:$RUN_PORT"
