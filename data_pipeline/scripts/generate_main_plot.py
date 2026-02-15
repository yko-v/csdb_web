#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 12:27:07 2026

@author: fedora
"""

from astropy.time import Time
import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "cubsats.db"
PNG_PATH = BASE_DIR / 'app' / 'static' / 'charts'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    SELECT launch_at,
           COUNT(*) as total
    FROM spacecrafts
    GROUP BY launch_at
    ORDER BY launch_at
""")

rows = cursor.fetchall()

times = []
total = []
for r in rows:
    t = r[0]
    if len(str(t))!=0:
        times.append(t)
        total.append(r[1])
        

years = pd.Series(Time(times, format='unix').iso).str[:4]
D = pd.DataFrame({'y':years, 'n':total}).groupby('y').sum()

plt.figure(figsize=(12, 6))
plt.bar(D.index, D['n'], color='steelblue', alpha=0.75)
plt.grid(axis='y')
#plt.title('Количество выведенных на орбиту кубсатов')
plt.tight_layout()
plt.savefig(PNG_PATH / 'cubesats_per_year.png')



cursor.execute("""
    SELECT launch_at
    FROM launches
    GROUP BY launch_id
""")

rows2 = cursor.fetchall()


years2 = pd.Series(Time([r[0] for r in rows2], format='unix').iso).str[:4] 
D2 = years2.value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.bar(D2.index, D2.values, color='steelblue', alpha=0.75)
plt.grid(axis='y')
#plt.title('Количество запусков с кубсатами')
plt.tight_layout()
plt.savefig(PNG_PATH / 'launches_per_year.png')















