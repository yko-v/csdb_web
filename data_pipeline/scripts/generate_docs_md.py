#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 00:49:55 2025

@author: ChatGPT + fedora
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import os

FIELDS_PATH = os.path.join("..", 'schemas/fields.yaml')
TABLES_PATH = os.path.join("..", 'schemas/tables.yaml')

OUTPUT_ROOT = os.path.join("../..", "docs")
FIELDS_MD = os.path.join(OUTPUT_ROOT, "fields.md")
TABLES_DIR = os.path.join(OUTPUT_ROOT, "tables")

os.makedirs(OUTPUT_ROOT, exist_ok=True)
os.makedirs(TABLES_DIR, exist_ok=True)

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def generate_field_block(name, attrs):
    md = f"## {name}\n"
    for key, value in attrs.items():
        md += f"- **{key.capitalize()}**: {value}\n"
    md += "\n"
    return md

def generate_fields_md(fields):
    md = "# Справочник полей\n\n"
    for field_name, attrs in fields.items():
        md += generate_field_block(field_name, attrs)
        md += "---\n\n"
    write(FIELDS_MD, md)

def generate_table_md(table_name, table_def, fields):
    md = []
    md.append(f"# Таблица `{table_name}`\n")

    # Определяем PK — первое поле
    first = table_def["fields"][0]
    pk = first["name"] if isinstance(first, dict) else first
    md.append(f"**Первичный ключ:** `{pk}`\n")

    md.append("\n## Поля\n")
    md.append("| Поле | Тип | Описание |")
    md.append("|------|------|-----------|")
    
    for f in table_def["fields"]:
        name = f["name"] if isinstance(f, dict) else f
        info = fields.get(name, {})
        f_type = info.get("type", "")
        descr = info.get("description", "")
    
        link = f"[{name}](../fields#{name.lower()})"
        md.append(f"| {link} | {f_type} | {descr} |")


    md.append("")

    # Foreign keys
    if "foreign_keys" in table_def:
        md.append("## Внешние ключи\n")
        for fk in table_def["foreign_keys"]:
            col = fk["column"]
            ref = fk["references"]
            md.append(f"- `{col}` → `{ref['table']}.{ref['column']}`")
        md.append("")

    # Indexes
    if "indexes" in table_def:
        md.append("## Индексы\n")
        for idx in table_def["indexes"]:
            name = idx["name"]
            cols = ", ".join(idx["columns"])
            md.append(f"- **{name}**: {cols}")
        md.append("")

    text = "\n".join(md)
    write(f"{TABLES_DIR}/{table_name}.md", text)

def main():  
    fields = load_yaml(FIELDS_PATH)
    tables = load_yaml(TABLES_PATH)

    generate_fields_md(fields)

    for table_name, table_def in tables.items():
        generate_table_md(table_name, table_def, fields)

    print("Generated fields.md and tables/*.md")

if __name__ == "__main__":
    main()

