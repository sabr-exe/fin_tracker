# 💰 Fin Tracker - Трекер курсов валют

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

Проект для отслеживания курсов валют в реальном времени с использованием Django, Docker, Celery и Redis.

## ✨ Особенности

- 📊 **Графики курсов** в реальном времени (Chart.js)
- 🔄 **Автоматическое обновление** курсов через Celery задачи
- 🐳 **Docker-контейнеризация** всего стека
- 💾 **PostgreSQL** для хранения данных
- ⚡ **Redis** как брокер для Celery
- 🔒 **Защита от CSRF** атак
- 📱 **Адаптивный дизайн**

## 🏗️ Архитектура

Архитектура:
- Django App ←→ PostgreSQL (база данных)
- Django App ←→ Redis (кеш и брокер для Celery)
- Всё запускается через Docker Compose

## 🚀 Быстрый старт

### Предварительные требования
- Docker & Docker Compose
- Python 3.11+ (для разработки без Docker)

### Установка
```bash
# 1. Клонируй репозиторий
git clone https://github.com/sabr-exe/fin_tracker.git
cd fin_tracker
# 2. Запусти через Docker
docker-compose up -d
# 3. Открой в браузере
http://localhost:8000/chart/

### Для разработки
# Создай виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Установи зависимости
pip install -r requirements.txt

# Настрой переменные окружения
cp .env.example .env

# Запусти миграции
python manage.py migrate

# Запусти сервер
python manage.py runserver

### 📁 Структура проекта
fin_tracker/
├── config/              # Настройки Django
├── rates/               # Приложение курсов валют
│   ├── models.py       # Модель CurrencyRate
│   ├── views.py        # View для графиков и API
│   ├── tasks.py        # Celery задачи
│   └── templates/      # HTML шаблоны
├── docker-compose.yml   # Docker конфигурация
├── Dockerfile          # Образ Django
├── requirements.txt    # Python зависимости
└── README.md          # Этот файл

### 🔧 API Endpoints
Метод	Endpoint	Описание
GET	/chart/	График курса валют
GET	/api/get-rates/	JSON данных для графика
POST	/api/refresh-rates/	Запуск обновления курсов

### 🐳 Docker сервисы
services:
  web:      # Django приложение
  db:       # PostgreSQL база данных
  redis:    # Кеш и брокер для Celery
  worker:   # Celery воркер
  beat:     # Celery beat (планировщик)

📈 Пример использования
Выбери валюту из выпадающего списка (USD, EUR, RUB, BYN)

Смотри график изменения курса за последние 30 обновлений

Обновляй данные кнопкой "Обновить"

Анализируй статистику: текущий, мин, макс курс

🤝 Вклад в проект
Форкни репозиторий

Создай ветку: git checkout -b feature/amazing-feature

Запуш изменения: git push origin feature/amazing-feature

Открой Pull Request

📄 Лицензия
MIT License - смотри файл LICENSE

👤 Автор
sabr-exe

GitHub: @sabr-exe

🙏 Благодарности
Chart.js для красивых графиков

exchangerate-api.com за API курсов

Сообщество Django за отличный фреймворк
