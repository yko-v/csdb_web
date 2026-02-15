# Таблица `spacecraft_models`

**Первичный ключ:** `model_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [model_id](../fields#model_id) | INTEGER | Идентификатор модели КА |
| [name](../fields#name) | VARCHAR | текстовое имя |
| [size](../fields#size) | REAL | размер (например, габариты) |
| [solar_panels](../fields#solar_panels) | INTEGER | число солнечных панелей |

## Внешние ключи

- `model_id` → `spacecrafts.model_id`
