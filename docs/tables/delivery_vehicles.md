# Таблица `delivery_vehicles`

**Первичный ключ:** `delivery_vehicle_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [delivery_vehicle_id](../fields#delivery_vehicle_id) | INTEGER | ид транспортного средства доставки |
| [name](../fields#name) | VARCHAR | текстовое имя |

## Внешние ключи

- `delivery_vehicle_id` → `delivery_methods.delivery_vehicle_id`

## Индексы

- **dispensers_index_0**: type_id
