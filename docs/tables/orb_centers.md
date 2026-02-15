# Таблица `orb_centers`

**Первичный ключ:** `orb_center_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [orb_center_id](../fields#orb_center_id) | INTEGER | Идентификатор притягивающего центра орбиты КА |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `orb_center_id` → `spacecrafts.orb_center_id`
