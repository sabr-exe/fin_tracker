# Берем легкий образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Запрещаем Python писать файлы .pyc и включаем немедленный вывод логов
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Устанавливаем gunicorn
RUN pip install gunicorn

# Запускаем сервер (замени 'config' на имя папки, где лежит wsgi.py)
#CMD ["python manage.py migrate", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:10000"]
CMD python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-10000}
