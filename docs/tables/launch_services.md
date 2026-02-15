# Таблица `launch_services`

**Первичный ключ:** `launch_service_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [launch_service_id](../fields#launch_service_id) | INTEGER | ид сервиса запуска |
| [launch_service_name](../fields#launch_service_name) | VARCHAR | название поставщика услуг запуска |

## Внешние ключи

- `launch_service_id` → `spacecrafts.launch_service_id`
