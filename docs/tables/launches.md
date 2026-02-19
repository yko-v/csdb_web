# Таблица `launches`

**Первичный ключ:** `launch_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [launch_id](../fields#launch_id) | VARCHAR(8) | Идентификатор запуска |
| [launch_at](../fields#launch_at) | TIMESTAMP | Дата запуска |
| [rocket_id](../fields#rocket_id) | INTEGER | ид ракетного агрегата |
| [launchpad_id](../fields#launchpad_id) | INTEGER | ид пусковой площадки |
| [state_id](../fields#state_id) | INTEGER | Идентификатор статуса запуска |

## Индексы

- **launches_index_0**: launch_at
- **launches_index_1**: rocket_id
- **launches_index_2**: launchpad_id
