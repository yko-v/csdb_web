# Таблица `states`

**Первичный ключ:** `state_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [state_id](../fields#state_id) | INTEGER | Идентификатор статуса запуска |
| [state](../fields#state) | VARCHAR | статус запуска |

## Внешние ключи

- `state_id` → `launches.state_id`
- `state_id` → `spacecrafts.state_id`
