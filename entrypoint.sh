#!/bin/bash

echo "Выполняем миграции..."
python manage.py migrate --noinput
echo "Запускаем сервер Uvicorn..."
exec uvicorn config.asgi:application --host 0.0.0.0 --port 8000