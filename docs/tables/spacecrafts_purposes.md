# Таблица `spacecrafts_purposes`

**Первичный ключ:** `purpose_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [purpose_id](../fields#purpose_id) | INTEGER | ид цели |
| [purpose_name_en](../fields#purpose_name_en) | TEXT | описание цели на английском |
| [purpose_name_ru](../fields#purpose_name_ru) | TEXT | описание цели на русском |

## Внешние ключи

- `purpose_id` → `spacecraft_families.purpose_id`
