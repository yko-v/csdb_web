# Таблица `delivery_methods`

**Первичный ключ:** `delivery_method_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [delivery_method_id](../fields#delivery_method_id) | INTEGER | Идентификатор метода доставки |
| [dispenser_id](../fields#dispenser_id) | INTEGER | ид диспенсера |
| [payload_id](../fields#payload_id) | INTEGER | ид полезной нагрузки |
| [delivery_vehicle_id](../fields#delivery_vehicle_id) | INTEGER | ид транспортного средства доставки |
| [iss_relation_id](../fields#iss_relation_id) | INTEGER | ид отношений с МКС |
| [separation_method_id](../fields#separation_method_id) | INTEGER | ид метода отделения |

## Внешние ключи

- `delivery_method_id` → `spacecrafts.delivery_method_id`
