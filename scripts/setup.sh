#!/bin/bash
set -e  # остановка при ошибке

# Перейти в папку скрипта
cd "$(dirname "$0")"

# Создать виртуальное окружение
python3 -m venv ../venv

# Активировать виртуальное окружение
. ../venv/bin/activate

# Установить зависимости
pip install -r ../requirements.txt

# Деактивировать виртуальное окружение
deactivate
