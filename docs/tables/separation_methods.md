# Таблица `separation_methods`

**Первичный ключ:** `separation_method_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [separation_method_id](../fields#separation_method_id) | INTEGER | ид метода отделения |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `separation_method_id` → `delivery_methods.separation_method_id`

## Индексы

- **separation_method_index_type**: type_id
