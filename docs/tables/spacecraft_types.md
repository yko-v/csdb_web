# Таблица `spacecraft_types`

**Первичный ключ:** `spacecraft_type_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [spacecraft_type_id](../fields#spacecraft_type_id) | INTEGER | Тип КА (кубсат, разгонный блок и т.д.) |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `spacecraft_type_id` → `spacecrafts.spacecraft_type_id`
