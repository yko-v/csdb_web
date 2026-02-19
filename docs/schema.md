# Структура базы данных

## Таблицы

| Таблица | Описание |
|---------|-----------|
| [spacecrafts](docs/tables/spacecrafts) |  |
| [spacecraft_names](docs/tables/spacecraft_names) |  |
| [spacecraft_types](docs/tables/spacecraft_types) |  |
| [spacecraft_families](docs/tables/spacecraft_families) |  |
| [spacecrafts_purposes](docs/tables/spacecrafts_purposes) |  |
| [spacecraft_models](docs/tables/spacecraft_models) |  |
| [add_elements](docs/tables/add_elements) |  |
| [platforms](docs/tables/platforms) |  |
| [states](docs/tables/states) |  |
| [launches](docs/tables/launches) |  |
| [rockets](docs/tables/rockets) |  |
| [rocket_families](docs/tables/rocket_families) |  |
| [spaceports](docs/tables/spaceports) |  |
| [launchpads](docs/tables/launchpads) |  |
| [delivery_methods](docs/tables/delivery_methods) |  |
| [delivery_vehicles](docs/tables/delivery_vehicles) |  |
| [dispensers](docs/tables/dispensers) |  |
| [iss_relations](docs/tables/iss_relations) |  |
| [payloads](docs/tables/payloads) |  |
| [separation_methods](docs/tables/separation_methods) |  |
| [base_cs](docs/tables/base_cs) |  |
| [launch_methods](docs/tables/launch_methods) |  |
| [states_orbit](docs/tables/states_orbit) |  |
| [orb_centers](docs/tables/orb_centers) |  |
| [programs](docs/tables/programs) |  |
| [organization_types](docs/tables/organization_types) |  |
| [countries](docs/tables/countries) |  |
| [launch_services](docs/tables/launch_services) |  |
| [orbital_events](docs/tables/orbital_events) |  |

## Связи между таблицами

### spacecrafts

- `spacecrafts.norad_id` → `orbital_events.norad_id`
- `spacecrafts.launch_method_id` → `launch_methods.launch_method_id`
- `spacecrafts.organization_type_id` → `organization_types.organization_type_id`
- `spacecrafts.spacecraft_id` → `spacecraft_names.spacecraft_id`
- `spacecrafts.primary_name_id` → `spacecraft_names.name_id`
- `spacecrafts.platform_id` → `platforms.platform_id`
- `spacecrafts.program_id` → `programs.program_id`

### spacecraft_names

- `spacecraft_names.spacecraft_id` → `spacecrafts.spacecraft_id`

### spacecraft_types

- `spacecraft_types.spacecraft_type_id` → `spacecrafts.spacecraft_type_id`

### spacecraft_families

- `spacecraft_families.family_id` → `spacecrafts.family_id`

### spacecrafts_purposes

- `spacecrafts_purposes.purpose_id` → `spacecraft_families.purpose_id`

### spacecraft_models

- `spacecraft_models.model_id` → `spacecrafts.model_id`

### add_elements

- `add_elements.add_element_id` → `spacecrafts.add_element_id`

### states

- `states.state_id` → `launches.state_id`
- `states.state_id` → `spacecrafts.state_id`

### rockets

- `rockets.rocket_id` → `launches.rocket_id`

### rocket_families

- `rocket_families.rocket_family_id` → `rockets.rocket_family_id`

### spaceports

- `spaceports.spaceport_id` → `launchpads.spaceport_id`
- `spaceports.spaceport_id` → `spacecrafts.spaceport_id`

### launchpads

- `launchpads.launchpad_id` → `launches.launchpad_id`

### delivery_methods

- `delivery_methods.delivery_method_id` → `spacecrafts.delivery_method_id`

### delivery_vehicles

- `delivery_vehicles.delivery_vehicle_id` → `delivery_methods.delivery_vehicle_id`

### dispensers

- `dispensers.dispenser_id` → `delivery_methods.dispenser_id`

### iss_relations

- `iss_relations.iss_relation_id` → `delivery_methods.iss_relation_id`

### payloads

- `payloads.payload_id` → `delivery_methods.payload_id`

### separation_methods

- `separation_methods.separation_method_id` → `delivery_methods.separation_method_id`

### base_cs

- `base_cs.base_spacecraft_id` → `spacecrafts.base_spacecraft_id`

### states_orbit

- `states_orbit.state_orbit_id` → `spacecrafts.state_orbit_id`

### orb_centers

- `orb_centers.orb_center_id` → `spacecrafts.orb_center_id`

### countries

- `countries.country_id` → `spacecrafts.develop_country_id`

### launch_services

- `launch_services.launch_service_id` → `spacecrafts.launch_service_id`

## Справочник полей

- [fields](docs/fields)
