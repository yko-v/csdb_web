# Таблица `countries`

**Первичный ключ:** `country_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [country_id](../fields#country_id) | INTEGER | ид страны |
| [en_name_cut](../fields#en_name_cut) | VARCHAR | Сокращенное название страны на английском |
| [country_name_en](../fields#country_name_en) | VARCHAR | название страны на английском |
| [country_name_ru](../fields#country_name_ru) | VARCHAR | название страны на русском |

## Внешние ключи

- `country_id` → `spacecrafts.develop_country_id`
