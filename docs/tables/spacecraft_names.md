# Таблица `spacecraft_names`

**Первичный ключ:** `name_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [name_id](../fields#name_id) | INTEGER | PK для spacecraft_names |
| [spacecraft_id](../fields#spacecraft_id) | INTEGER | Идентификатор космического аппарата |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `spacecraft_id` → `spacecrafts.spacecraft_id`

## Индексы

- **spacecraft_id_index**: spacecraft_id
- **spacecraft_name_index**: name
