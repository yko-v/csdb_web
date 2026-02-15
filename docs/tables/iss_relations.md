# Таблица `iss_relations`

**Первичный ключ:** `iss_relation_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [iss_relation_id](../fields#iss_relation_id) | INTEGER | ид отношений с МКС |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `iss_relation_id` → `delivery_methods.iss_relation_id`

## Индексы

- **iss_relations_index_type**: type_id
