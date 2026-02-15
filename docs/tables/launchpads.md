# Таблица `launchpads`

**Первичный ключ:** `launchpad_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [launchpad_id](../fields#launchpad_id) | INTEGER | ид пусковой площадки |
| [name](../fields#name) | VARCHAR | текстовое имя |
| [spaceport_id](../fields#spaceport_id) | INTEGER | Идентификатор космодрома |
| [long](../fields#long) | REAL | Долгота |
| [lat](../fields#lat) | REAL | Широта |

## Внешние ключи

- `launchpad_id` → `launches.launchpad_id`

## Индексы

- **launchpads_index_0**: spaceport_id
