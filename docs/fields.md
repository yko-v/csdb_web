# Справочник полей

## spacecraft_id
- **Type**: INTEGER
- **Description**: Идентификатор космического аппарата
- **Definition**: Номер
- **Host**: КА
- **Object**: КА

---

## primary_name_id
- **Type**: INTEGER
- **Description**: Ссылка на номер основного (primary) названия КА name_id в таблице spacecraft_names
- **Definition**: Название
- **Host**: КА
- **Object**: КА

---

## spacecraft_type_id
- **Type**: INTEGER
- **Description**: Тип КА (кубсат, разгонный блок и т.д.)
- **Definition**: Тип
- **Host**: КА
- **Object**: КА

---

## family_id
- **Type**: INTEGER
- **Description**: Идентификатор семейства КА
- **Definition**: Номер
- **Host**: Семейство КА
- **Object**: КА

---

## mass
- **Type**: REAL
- **Description**: Масса
- **Definition**: Физическая величина
- **Host**: КА
- **Object**: КА
- **Units**: кг

---

## model_id
- **Type**: INTEGER
- **Description**: Идентификатор модели КА
- **Definition**: Номер
- **Host**: Модель КА
- **Object**: КА

---

## add_element_id
- **Type**: INTEGER
- **Description**: Идентификатор дополнительного элемента конструкции КА
- **Definition**: Номер
- **Host**: Элемент конструкции КА
- **Object**: КА

---

## platform_id
- **Type**: INTEGER
- **Description**: Идентификатор спутниковой платформы
- **Definition**: Номер
- **Host**: Спутниковая платформа
- **Object**: КА

---

## delivery_method_id
- **Type**: INTEGER
- **Description**: Идентификатор метода доставки
- **Definition**: Номер
- **Host**: Метод доставки КА
- **Object**: КА

---

## launch_method_id
- **Type**: INTEGER
- **Description**: Идентификатор способа запуска
- **Definition**: Номер
- **Host**: Метод запуска КА
- **Object**: КА

---

## base_spacecraft_id
- **Type**: INTEGER
- **Description**: Идентификатор базового космического аппарата
- **Definition**: Номер
- **Host**: Базовый КА
- **Object**: КА

---

## state_orbit_id
- **Type**: INTEGER
- **Description**: Cтатус орбитального движения
- **Definition**: Номер
- **Host**: Статус орбиты КА
- **Object**: КА

---

## norad_id
- **Type**: INTEGER
- **Description**: Идентификатор КА NORAD
- **Definition**: Номер
- **Host**: NORAD КА
- **Object**: КА

---

## on_orbit_at
- **Type**: TIMESTAMP
- **Description**: Дата начала наблюдения по TLE
- **Definition**: Дата
- **Host**: Орбита КА
- **Object**: КА

---

## decay_at
- **Type**: TIMESTAMP
- **Description**: Дата окончания наблюдений по TLE
- **Definition**: Дата
- **Host**: Орбита КА
- **Object**: КА

---

## orb_center_id
- **Type**: INTEGER
- **Description**: Идентификатор притягивающего центра орбиты КА
- **Definition**: Дата
- **Host**: Орбита КА
- **Object**: КА

---

## orbit_init_altitude
- **Type**: REAL
- **Description**: Начальная высота орбиты КА по TLE
- **Definition**: Высота орбиты
- **Host**: Орбита КА
- **Object**: КА
- **Units**: км

---

## orbit_init_period
- **Type**: REAL
- **Description**: Начальный период орбиты КА по TLE
- **Definition**: Период орбиты
- **Host**: Орбита КА
- **Object**: КА
- **Units**: минуты

---

## orbit_init_ecs
- **Type**: REAL
- **Description**: Начальный эксцентриситет орбиты КА по TLE
- **Definition**: Эксцентриситет
- **Host**: Орбита КА
- **Object**: КА

---

## orbit_init_inc
- **Type**: REAL
- **Description**: Начальное наклонение орбиты КА по TLE
- **Definition**: Наклонение
- **Host**: Орбита КА
- **Object**: КА
- **Units**: Градусы

---

## state_id
- **Type**: INTEGER
- **Description**: Идентификатор статуса запуска
- **Definition**: Номер
- **Host**: Статус запуска
- **Object**: РН

---

## launch_id
- **Type**: VARCHAR(8)
- **Description**: Идентификатор запуска
- **Format**: ['yyyy-nnn, если запуск успех (Suc.)', 'yyyy-Fnn, если запуск провал (Fail)', 'nn = номер запуска в году yyyy']
- **Definition**: Номер
- **Host**: Запуск
- **Object**: РН

---

## cospar_id
- **Type**: INTEGER
- **Description**: Идентификатор КА COSPAR
- **Definition**: Номер
- **Host**: COSPAR КА
- **Object**: КА

---

## launch_at
- **Type**: TIMESTAMP
- **Description**: Дата запуска
- **Definition**: Дата
- **Host**: Запуск
- **Comments**: В один день может быть несколько запусков
- **Object**: РН

---

## spaceport_id
- **Type**: INTEGER
- **Description**: Идентификатор космодрома
- **Definition**: Номер
- **Host**: Космодром
- **Object**: Космодром

---

## long
- **Type**: REAL
- **Description**: Долгота

---

## lat
- **Type**: REAL
- **Description**: Широта

---

## launch_service_id
- **Type**: INTEGER
- **Description**: ид сервиса запуска

---

## organization_type_id
- **Type**: INTEGER
- **Description**: тип организации

---

## program_id
- **Type**: INTEGER
- **Description**: ид программы

---

## develop_country_id
- **Type**: INTEGER
- **Description**: ид страны разработки

---

## space_rocket_link
- **Type**: TEXT
- **Description**: ссылка на описание в сети

---

## nanosats_link
- **Type**: TEXT
- **Description**: ссылка на nanosats

---

## link
- **Type**: TEXT
- **Description**: ссылка на nanosats

---

## name_id
- **Type**: INTEGER
- **Description**: PK для spacecraft_names

---

## name
- **Type**: VARCHAR
- **Description**: текстовое имя

---

## purpose_id
- **Type**: INTEGER
- **Description**: ид цели

---

## size
- **Type**: REAL
- **Description**: размер (например, габариты)

---

## solar_panels
- **Type**: INTEGER
- **Description**: число солнечных панелей

---

## has_hood
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_large_antenna
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_depl_solar_panels
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_thruster
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_add_mass
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_door
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_tape
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_teather
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_cylidner
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_rod
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_sail
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_panel
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_balloon
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## has_pyramid
- **Type**: BOOLEAN
- **Description**: есть ли капот

---

## rocket_id
- **Type**: INTEGER
- **Description**: ид ракетного агрегата

---

## rocket_family_id
- **Type**: INTEGER
- **Description**: ид семейства ракет

---

## country_id
- **Type**: INTEGER
- **Description**: ид страны

---

## launchpad_id
- **Type**: INTEGER
- **Description**: ид пусковой площадки

---

## dispenser_id
- **Type**: INTEGER
- **Description**: ид диспенсера

---

## payload_id
- **Type**: INTEGER
- **Description**: ид полезной нагрузки

---

## separation_method_id
- **Type**: INTEGER
- **Description**: ид метода отделения

---

## delivery_vehicle_id
- **Type**: INTEGER
- **Description**: ид транспортного средства доставки

---

## iss_relation_id
- **Type**: INTEGER
- **Description**: ид отношений с МКС

---

## dispenser_name
- **Type**: VARCHAR
- **Description**: название диспенсера

---

## id
- **Type**: INTEGER
- **Description**: PK для orbital_events

---

## eccentricity
- **Type**: REAL

---

## inclination
- **Type**: REAL

---

## mean_anomaly
- **Type**: REAL

---

## perigee_arg
- **Type**: REAL

---

## asend_node_long
- **Type**: REAL

---

## mean_motion
- **Type**: REAL

---

## mean_motion_1der
- **Type**: REAL

---

## mean_motion_2der
- **Type**: REAL

---

## rad_pressure_coef
- **Type**: REAL

---

## event_at
- **Type**: TIMESTAMP

---

## period
- **Type**: REAL

---

## semi_major_axis
- **Type**: REAL

---

## altitude
- **Type**: REAL

---

## perigee_altitude
- **Type**: REAL

---

## apogee_altitude
- **Type**: REAL

---

## created_at
- **Type**: TIMESTAMP
- **Description**: время создания

---

## updated_at
- **Type**: TIMESTAMP
- **Description**: время обновления

---

## purpose_name_en
- **Type**: TEXT
- **Description**: описание цели на английском

---

## purpose_name_ru
- **Type**: TEXT
- **Description**: описание цели на русском

---

## state
- **Type**: VARCHAR
- **Description**: статус запуска

---

## description
- **Type**: TEXT
- **Description**: описание

---

## organization_type_name
- **Type**: VARCHAR
- **Description**: название разработчика

---

## launch_service_name
- **Type**: VARCHAR
- **Description**: название поставщика услуг запуска

---

## country_name_en
- **Type**: VARCHAR
- **Description**: название страны на английском

---

## country_name_ru
- **Type**: VARCHAR
- **Description**: название страны на русском

---

## en_name_cut
- **Type**: VARCHAR
- **Description**: Сокращенное название страны на английском

---

