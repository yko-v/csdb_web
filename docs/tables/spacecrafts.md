# Таблица `spacecrafts`

**Первичный ключ:** `spacecraft_id`


## Поля

| Поле | Тип | Описание |
|------|------|-----------|
| [spacecraft_id](../fields#spacecraft_id) | INTEGER | Идентификатор космического аппарата |
| [primary_name_id](../fields#primary_name_id) | INTEGER | Ссылка на номер основного (primary) названия КА name_id в таблице spacecraft_names |
| [spacecraft_type_id](../fields#spacecraft_type_id) | INTEGER | Тип КА (кубсат, разгонный блок и т.д.) |
| [family_id](../fields#family_id) | INTEGER | Идентификатор семейства КА |
| [model_id](../fields#model_id) | INTEGER | Идентификатор модели КА |
| [add_element_id](../fields#add_element_id) | INTEGER | Идентификатор дополнительного элемента конструкции КА |
| [delivery_method_id](../fields#delivery_method_id) | INTEGER | Идентификатор метода доставки |
| [mass](../fields#mass) | REAL | Масса |
| [launch_at](../fields#launch_at) | TIMESTAMP | Дата запуска |
| [cospar_id](../fields#cospar_id) | INTEGER | Идентификатор КА COSPAR |
| [launch_id](../fields#launch_id) | VARCHAR(8) | Идентификатор запуска |
| [spaceport_id](../fields#spaceport_id) | INTEGER | Идентификатор космодрома |
| [on_orbit_at](../fields#on_orbit_at) | TIMESTAMP | Дата начала наблюдения по TLE |
| [norad_id](../fields#norad_id) | INTEGER | Идентификатор КА NORAD |
| [state_id](../fields#state_id) | INTEGER | Идентификатор статуса запуска |
| [state_orbit_id](../fields#state_orbit_id) | INTEGER | Cтатус орбитального движения |
| [decay_at](../fields#decay_at) | TIMESTAMP | Дата окончания наблюдений по TLE |
| [orbit_init_altitude](../fields#orbit_init_altitude) | REAL | Начальная высота орбиты КА по TLE |
| [orbit_init_period](../fields#orbit_init_period) | REAL | Начальный период орбиты КА по TLE |
| [orbit_init_ecs](../fields#orbit_init_ecs) | REAL | Начальный эксцентриситет орбиты КА по TLE |
| [orbit_init_inc](../fields#orbit_init_inc) | REAL | Начальное наклонение орбиты КА по TLE |
| [orb_center_id](../fields#orb_center_id) | INTEGER | Идентификатор притягивающего центра орбиты КА |
| [launch_method_id](../fields#launch_method_id) | INTEGER | Идентификатор способа запуска |
| [launch_service_id](../fields#launch_service_id) | INTEGER | ид сервиса запуска |
| [organization_type_id](../fields#organization_type_id) | INTEGER | тип организации |
| [platform_id](../fields#platform_id) | INTEGER | Идентификатор спутниковой платформы |
| [program_id](../fields#program_id) | INTEGER | ид программы |
| [develop_country_id](../fields#develop_country_id) | INTEGER | ид страны разработки |
| [base_spacecraft_id](../fields#base_spacecraft_id) | INTEGER | Идентификатор базового космического аппарата |
| [space_rocket_link](../fields#space_rocket_link) | TEXT | ссылка на описание в сети |
| [nanosats_link](../fields#nanosats_link) | TEXT | ссылка на nanosats |

## Внешние ключи

- `norad_id` → `orbital_events.norad_id`
- `launch_method_id` → `launch_methods.launch_method_id`
- `organization_type_id` → `organization_types.organization_type_id`
- `spacecraft_id` → `spacecraft_names.spacecraft_id`
- `primary_name_id` → `spacecraft_names.name_id`
- `platform_id` → `platforms.platform_id`
- `program_id` → `programs.program_id`

## Индексы

- **cospar_id_index**: cospar_id
- **spacecrafts_index_1**: spacecraft_type_id
- **spacecrafts_index_2**: family_id
- **spacecrafts_index_3**: model_id
- **spacecrafts_index_4**: launch_at
- **spacecrafts_index_5**: norad_id
- **spacecrafts_index_6**: on_orbit_at
- **spacecrafts_index_7**: orb_center_id
- **spacecrafts_index_8**: launch_method_id
- **spacecrafts_index_9**: decay_at
- **platform_id_index**: platform_id
- **program_id_index**: program_id
- **spacecrafts_index_10**: decay_at
