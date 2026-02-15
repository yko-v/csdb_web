# Таблица `rockets`

**Первичный ключ:** `rocket_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [rocket_id](../fields#rocket_id) | INTEGER | ид ракетного агрегата |
| [name](../fields#name) | VARCHAR | текстовое имя |
| [rocket_family_id](../fields#rocket_family_id) | INTEGER | ид семейства ракет |

## Внешние ключи

- `rocket_id` → `launches.rocket_id`
