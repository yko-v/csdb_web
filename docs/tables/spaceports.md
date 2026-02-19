# Таблица `spaceports`

**Первичный ключ:** `spaceport_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [spaceport_id](../fields#spaceport_id) | INTEGER | Идентификатор космодрома |
| [name](../fields#name) | VARCHAR | текстовое имя |
| [long](../fields#long) | REAL | Долгота |
| [lat](../fields#lat) | REAL | Широта |
| [country_id](../fields#country_id) | INTEGER | ид страны |

## Внешние ключи

- `spaceport_id` → `launchpads.spaceport_id`
- `spaceport_id` → `spacecrafts.spaceport_id`
