# Используем официальный Python-образ
FROM python:3.13.3

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Команда по умолчанию (можно переопределить в docker-compose)
CMD ["gunicorn", "arscityapi.wsgi:application", "--bind", "0.0.0.0:8000"]
