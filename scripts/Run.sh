cd /var/www/csdb || exit 1
. venv/bin/activate
export PYTHONPATH=$(pwd)  # добавляем корень проекта в пути
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
