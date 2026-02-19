# Таблица `spacecraft_families`

**Первичный ключ:** `family_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [family_id](../fields#family_id) | INTEGER | Идентификатор семейства КА |
| [name](../fields#name) | VARCHAR | текстовое имя |
| [purpose_id](../fields#purpose_id) | INTEGER | ид цели |

## Внешние ключи

- `family_id` → `spacecrafts.family_id`

## Индексы

- **spacecraft_families_index_0**: purpose_id
