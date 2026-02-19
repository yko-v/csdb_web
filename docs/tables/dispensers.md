# Таблица `dispensers`

**Первичный ключ:** `dispenser_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [dispenser_id](../fields#dispenser_id) | INTEGER | ид диспенсера |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `dispenser_id` → `delivery_methods.dispenser_id`
