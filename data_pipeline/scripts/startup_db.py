import os
import sys
import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

db_name = 'database/cubsats.db'

def get_project_root_from_venv():
    return Path(sys.prefix).parent

def get_tables_path(pip_path) -> str:
    tables_path = pip_path / 'data/processed/' #None
   
    SQL_path = pip_path / 'data/generate_db.sql'
    print(SQL_path)
    return tables_path, SQL_path

def create_db(db_path, SQL_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(SQL_path, "r") as f:
        SQL = f.read()

    cursor.executescript(SQL)

def insert_data(db_path, tables_path, batch_size=500):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    tables_path = Path(tables_path)
    csv_files = [f for f in os.listdir(tables_path) if f.lower().endswith(".csv")]
    print("CSV-файлы для загрузки:", *csv_files)

    try:
        conn.execute("BEGIN TRANSACTION;")  # Начинаем транзакцию

        for filename in csv_files:
            csv_path = tables_path / filename
            table_name = os.path.splitext(filename)[0]

            with open(csv_path, "r", encoding="utf-8", newline="") as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # первая строка — заголовки
                insert_stmt = f"INSERT OR REPLACE INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(['?'] * len(headers))});"
                print(f"Загружаем в таблицу {table_name}: {insert_stmt}")

                batch = []
                for row in reader:
                    if any(row):  # пропускаем пустые строки
                        batch.append(row)
                        if len(batch) >= batch_size:
                            cursor.executemany(insert_stmt, batch)
                            batch.clear()

                # Вставляем оставшиеся строки
                if batch:
                    cursor.executemany(insert_stmt, batch)

        conn.commit()  # фиксируем все изменения после всех файлов
        print("✅ Все данные успешно вставлены.")

    except Exception as e:
        conn.rollback()
        print(f"❌ Ошибка при вставке: {e}")
        print("⚠️ Все изменения отменены.")

    finally:
        conn.close()

if __name__ == "__main__":
    db_path = BASE_DIR / db_name
    pip_path = BASE_DIR / 'data_pipeline'
    tables_path, SQL_path = get_tables_path(pip_path)
    
    create_db(db_path, SQL_path)
    insert_data(db_path, tables_path)