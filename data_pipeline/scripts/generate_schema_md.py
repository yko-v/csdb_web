#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 10:47:41 2025

@author: ChatGPT + fedora
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import os

TABLES_PATH = os.path.join("..", 'schemas/tables.yaml')

OUTPUT_ROOT = os.path.join("../..", "docs")
OUT = os.path.join(OUTPUT_ROOT, "schema.md") 
TABLES_DIR = os.path.join(OUTPUT_ROOT, "tables")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def generate_schema_doc(tables):
    md = []
    md.append("# Структура базы данных\n")

    md.append("## Таблицы\n")
    md.append("| Таблица | Описание |")
    md.append("|---------|-----------|")

    for t in tables:
        md.append(f"| [{t}](tables/{t}.md) |  |")

    md.append("")

    md.append("## Связи между таблицами\n")
    for t, defn in tables.items():
        if "foreign_keys" not in defn:
            continue

        md.append(f"### {t}\n")
        for fk in defn["foreign_keys"]:
            col = fk["column"]
            ref = fk["references"]
            md.append(f"- `{t}.{col}` → `{ref['table']}.{ref['column']}`")
        md.append("")

    md.append("## Справочник полей\n")
    md.append("- [fields.md](fields.md)")

    return "\n".join(md)

def main():
    tables = load_yaml(TABLES_PATH)

    schema_md = generate_schema_doc(tables)
    write(OUT, schema_md)
    print("Generated schema.md")

if __name__ == "__main__":
    main()















