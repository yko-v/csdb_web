# Таблица `orbital_events`

**Первичный ключ:** `id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [id](../fields#id) | INTEGER | PK для orbital_events |
| [norad_id](../fields#norad_id) | INTEGER | Идентификатор КА NORAD |
| [eccentricity](../fields#eccentricity) | REAL |  |
| [inclination](../fields#inclination) | REAL |  |
| [mean_anomaly](../fields#mean_anomaly) | REAL |  |
| [perigee_arg](../fields#perigee_arg) | REAL |  |
| [asend_node_long](../fields#asend_node_long) | REAL |  |
| [mean_motion](../fields#mean_motion) | REAL |  |
| [mean_motion_1der](../fields#mean_motion_1der) | REAL |  |
| [mean_motion_2der](../fields#mean_motion_2der) | REAL |  |
| [rad_pressure_coef](../fields#rad_pressure_coef) | REAL |  |
| [event_at](../fields#event_at) | TIMESTAMP |  |
| [period](../fields#period) | REAL |  |
| [semi_major_axis](../fields#semi_major_axis) | REAL |  |
| [altitude](../fields#altitude) | REAL |  |
| [perigee_altitude](../fields#perigee_altitude) | REAL |  |
| [apogee_altitude](../fields#apogee_altitude) | REAL |  |

## Индексы

- **norad_event_at_index**: norad_id, event_at
- **event_at_index**: event_at
