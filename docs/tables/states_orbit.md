# Таблица `states_orbit`

**Первичный ключ:** `state_orbit_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [state_orbit_id](../fields#state_orbit_id) | INTEGER | Cтатус орбитального движения |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `state_orbit_id` → `spacecrafts.state_orbit_id`
