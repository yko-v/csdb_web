# Таблица `payloads`

**Первичный ключ:** `payload_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [payload_id](../fields#payload_id) | INTEGER | ид полезной нагрузки |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `payload_id` → `delivery_methods.payload_id`

## Индексы

- **payloads_index_type**: type_id
