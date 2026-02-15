#!/bin/bash
cd "$(dirname "$(realpath "$0")")" || exit 1

. ../venv/bin/activate

echo "✅ Виртуальное окружение активировано"

# --- Запуск FastAPI ---
echo "🚀 Запуск FastAPI сервера..."
fastapi dev ../app/main.py  --host 0.0.0.0 --port 8000
