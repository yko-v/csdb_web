import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "cubsats.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()
