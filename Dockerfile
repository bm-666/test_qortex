FROM python:3.12-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости без виртуального окружения
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Копируем весь проект
COPY . /app

# Переходим в папку с manage.py
WORKDIR /app/src

# Делаем entrypoint исполняемым
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
