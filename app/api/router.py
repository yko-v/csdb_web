import json
import pandas as pd
import plotly.graph_objects as go
from fastapi import APIRouter, HTTPException

from app.db import db

cursor = db.cursor

router = APIRouter(prefix="/api")

@router.get("/overview")
async def overview():
    cursor.execute("SELECT COUNT(*) FROM spacecrafts")
    total_spacecraft = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM launches")
    total_launches = cursor.fetchone()[0]

    # пример — можно хранить в таблице metadata
    last_update = "2024-01-01"

    # пример данных для графика
    chart_data = {
        "labels": ["Аппараты", "Запуски"],
        "values": [total_spacecraft, total_launches]
    }

    return {
        "total_spacecraft": total_spacecraft,
        "total_launches": total_launches,
        "last_update": last_update,
        "chart": chart_data
    }


@router.get("/spacecraft_families")
async def get_spacecraft_families():
    cursor.execute("""
                   SELECT family_id AS '#', 
                       scf.name AS 'Семейство', 
                       COUNT(spacecraft_id) AS 'Количество КА', 
                       SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END) AS 'Успешных',
                       ROUND(SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END)*CAST(100 AS FLOAT)/COUNT(spacecraft_id)) AS 'Процент успеха',
                       space_rocket_link AS 'Ссылка на Spacerocket', 
                       nanosats_link AS 'Ссылка на Nanosats'
                   FROM spacecraft_families scf 
                   LEFT JOIN spacecrafts as sc USING(family_id) 
                   GROUP BY family_id
                   """
                   )
    #    GROUP_CONCAT(DISTINCT CAST(ROUND(size) AS INTEGER)) AS 'Объем (U)', 
                    #                   LEFT JOIN spacecraft_models scm USING(model_id) 
                    #LEFT JOIN spacecrafts_purposes scp USING(purpose_id) 
                        #scp.purpose_name_ru,
                        # NULL AS developer, NULL AS country,
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows
    }



# Разрешённые параметры для безопасности
ALLOWED_PARAMS = {
    "altitude",
    "inclination",
    "eccentricity",
    "semi_major_axis",
    "perigee_altitude",
    "apogee_altitude",
    "period",
    "mean_motion"
}

@router.get("/orbits_plot_json")
async def plot_orbit_json(norad_id: int, parameter: str):
    if parameter not in ALLOWED_PARAMS:
        raise HTTPException(status_code=400, detail="Invalid parameter")

    cursor.execute(f"""
        SELECT event_at, {parameter}
        FROM orbital_events
        WHERE norad_id = ?
        ORDER BY event_at
        LIMIT 5000
    """, (norad_id,))

    rows = cursor.fetchall()
    if not rows:
        return {"data": [], "layout": {}}

    df = pd.DataFrame(rows, columns=["event_at", "value"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["event_at"], y=df["value"], mode="lines", name=parameter))
    fig.update_layout(
        title=f"{parameter} для NORAD {norad_id}",
        xaxis_title="Дата",
        yaxis_title=parameter,
        height=600
    )

    return json.loads(fig.to_json())  # Возвращаем JSON для JS


@router.get("/launches")
async def launches():
    cursor.execute("""
                    SELECT 
                        l.launch_id AS 'COSPAR ID', 
                        strftime('%Y-%m-%d', datetime(l.launch_at, 'unixepoch')) AS 'Дата запуска', 
                        r.name AS 'Ракета-носитель', 
                        sp.name AS 'Космодром', 
                        lp.name AS 'Площадка', 
                        s.state AS 'Статус запуска', 
                        COUNT(spacecraft_id) AS 'Количество кубсатов'
                        
                    FROM launches l
                    LEFT JOIN rockets r USING(rocket_id)
                    LEFT JOIN launchpads lp USING(launchpad_id)
                    LEFT JOIN spaceports sp USING(spaceport_id)
                    LEFT JOIN spacecrafts sc USING(launch_id)
                    LEFT JOIN states s ON s.state_id=l.state_id
                    GROUP BY l.launch_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }

@router.get("/spaceports")
async def spaceports():
    cursor.execute("""
                    SELECT 
                        sp.spaceport_id AS '#', 
                        sp.name AS 'name',
                        sp.lat AS 'lat', 
                        sp.long AS 'long',
                        COUNT(*) AS 'Количество запусков с кубсатами', 
                        SUM(CASE WHEN l.state_id = 1 THEN 1 ELSE 0 END) AS 'Успешных запусков',
                        ROUND(SUM(CASE WHEN l.state_id = 1 THEN 1 ELSE 0 END)*CAST(100 AS FLOAT)/COUNT(*),2) AS 'Процент успеха'
                    FROM spaceports sp
                    LEFT JOIN launchpads lp USING(spaceport_id)
                    LEFT JOIN launches l USING(launchpad_id)
                    GROUP BY sp.spaceport_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }




@router.get("/rocket_families")
async def rocket_families():
    cursor.execute("""
                    SELECT rf.rocket_family_id, rf.name as rocket_family_name, 
                        COUNT(*) as launch_cnt, SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END) as succ_launch_cnt,
                        SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END)/COUNT(*)*100 as succ_rate
                    FROM rocket_families rf
                    LEFT JOIN rockets r USING(rocket_family_id)
                    LEFT JOIN launches l USING(rocket_id)
                    GROUP BY rf.rocket_family_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }


@router.get("/containers")
async def containers():
    cursor.execute("""
                    SELECT d.dispenser_id, d.name as dispenser_name,
                        COUNT(*) as launch_cnt, SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END) as succ_launch_cnt,
                        ROUND(SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END)*CAST(100 AS FLOAT)/COUNT(*),2) as succ_rate
                    FROM dispensers d
                    LEFT JOIN delivery_methods dm USING(dispenser_id)
                    LEFT JOIN spacecrafts sc USING(delivery_method_id)
                    GROUP BY d.dispenser_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }


@router.get("/base_cs")
async def base_cs():
    cursor.execute("""
                    SELECT bcs.base_spacecraft_id, bcs.name as base_cs_name,
                        COUNT(*) as launch_cnt, SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END) as succ_launch_cnt,
                        ROUND(SUM(CASE WHEN sc.state_orbit_id = 0 THEN 1 ELSE 0 END)*CAST(100 AS FLOAT)/COUNT(*),2) as succ_rate
                    FROM base_cs bcs
                    LEFT JOIN spacecrafts sc USING(base_spacecraft_id)
                    GROUP BY bcs.base_spacecraft_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }

@router.get("/missions")
async def missions():
    cursor.execute("""
                    SELECT sp.purpose_id, sp.purpose_name_ru,
                        COUNT(*) as launch_cnt
                    FROM spacecrafts_purposes sp
                    LEFT JOIN spacecraft_families dm USING(purpose_id)
                    LEFT JOIN spacecrafts sc USING(family_id)
                    GROUP BY sp.purpose_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }

@router.get("/programs")
async def programs():
    cursor.execute("""
                    SELECT p.program_id, p.name as program_name,
                        COUNT(*) as launch_cnt
                    FROM programs p
                    LEFT JOIN spacecrafts sc USING(program_id)
                    GROUP BY p.program_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }

@router.get("/platforms")
async def platforms():
    cursor.execute("""
                    SELECT p.platform_id, p.name as platform_name,
                        COUNT(DISTINCT sc.family_id) as launch_cnt
                    FROM platforms p
                    LEFT JOIN spacecrafts sc USING(platform_id)
                    GROUP BY p.platform_id
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }




@router.get("/orbits_init")
async def orbits_init():
    cursor.execute("""
        SELECT 
            scn.name AS 'Кубсат',
            so.name AS 'Статус орбиты',
            norad_id AS 'NORAD ID',
            orbit_init_altitude AS 'Высота, км',
            orbit_init_period AS 'Период, мин',
            orbit_init_ecs AS 'Эксцентриситет',
            orbit_init_inc AS 'Наклонение'
        FROM spacecrafts scf
        LEFT JOIN states_orbit so USING (state_orbit_id)
        LEFT JOIN spacecraft_names scn ON (scf.primary_name_id=scn.name_id)
                    """
                   )

            # decay_at,
            # on_orbit_at


    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }







@router.get("/db_info")
async def db_info():
    return 




'''
@router.get("/spacecraft_family")
async def get_spacecraft_family(id: int):
    cursor.execute(f"""SELECT scf.name, scp.purpose_name_ru, NULL as developer, NULL as country,
                        COUNT(spacecraft_id) as counts, SUM(CASE WHEN state_orbit_id = 0 THEN 1 ELSE 0 END) as suc,
                       ROUND(SUM(CASE WHEN state_orbit_id = 0 THEN 1 ELSE 0 END)*CAST(100 AS FLOAT)/COUNT(spacecraft_id), 2) as suc_perc,
                       space_rocket_link, nanosats_link
                   FROM spacecraft_families scf
                   LEFT JOIN spacecrafts_purposes scp USING(purpose_id)
                   LEFT JOIN spacecrafts as sc USING(family_id)
				   LEFT JOIN spacecraft_models scm USING(model_id)
				   WHERE family_id = {id}"""
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
        WITH norad_ids AS (
                SELECT norad_id
                FROM spacecrafts
                WHERE family_id = {id}
            ),
            ranked AS (
          SELECT
            oe.altitude, oe.perigee_altitude, oe.apogee_altitude, oe.norad_id,
            oe.semi_major_axis, oe.inclination, oe.eccentricity, oe.period,
            ROW_NUMBER() OVER (PARTITION BY oe.norad_id ORDER BY oe.event_at DESC) AS rn
          FROM orbital_events AS oe
		  JOIN norad_ids USING(norad_id)
        )
        SELECT sn.name as cubesat_name, sc.norad_id, cospar_id, 
                sc.state_id as cubesat_state_id, datetime(sc.launch_at, 'unixepoch') as launch_at, size, mass, 
                -- spc.name as solar_panel_config_name, 
                -- spc.description as solar_panel_config_description,
	            oe.altitude, oe.perigee_altitude, oe.apogee_altitude,
                oe.semi_major_axis, oe.inclination, oe.eccentricity, oe.period
        FROM spacecrafts as sc
		LEFT JOIN norad_ids USING(norad_id)
        LEFT JOIN ranked oe ON sc.norad_id = oe.norad_id AND oe.rn = 1
        LEFT JOIN spacecraft_names sn on sc.primary_name_id=sn.name_id
        LEFT JOIN spacecraft_models scf USING(model_id)
        -- LEFT JOIN solar_panels spc USING(solar_panel_id)
        WHERE family_id = {id}
        """
                   )

    cubesats = cursor.fetchall()
    cubesat_columns = [desc[0] for desc in cursor.description]
    return {
        "name": rows[0][0],
        "columns": columns,
        "rows": rows,
        "cubesat_rows": cubesats,
        "cubesat_columns": cubesat_columns,
    }

# Нужно будет добавить фильтр на Cubesats/CS_Family
@router.get("/spacecraft_family_names")
async def get_spacecraft_family_names():
    cursor.execute(f"""
                    SELECT name
                    FROM spacecraft_families
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return {
        "columns": columns,
        "rows": rows,
    }


@router.get("/launch_id")
async def get_launch(id: str):
    cursor.execute(f"""SELECT l.launch_id, datetime(l.launch_at, 'unixepoch') as launch_at, r.name AS rocket_name, 
                        sp.name AS spaceport_name, lp.name AS launchpad_name, 
                        s.state, COUNT(spacecraft_id) AS spacecrafts_cnt
                    FROM launches l
                    LEFT JOIN rockets r USING(rocket_id)
                    LEFT JOIN launchpads lp USING(launchpad_id)
                    LEFT JOIN spaceports sp USING(spaceport_id) 
                    LEFT JOIN spacecrafts sc USING(launch_id)
                    LEFT JOIN states s ON s.state_id=l.state_id
				    WHERE l.launch_id = "{id}" """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
        SELECT sc.spacecraft_id, sn.name as cubesat_name, 
            scf.name as family_name, scm.name as model_name,
            d.name as container, s.state
        FROM spacecrafts sc
        LEFT JOIN launches l USING(launch_id)
        LEFT JOIN spacecraft_names sn on sc.primary_name_id=sn.name_id
        LEFT JOIN spacecraft_families scf  USING(family_id)
        LEFT JOIN spacecraft_models scm  USING(model_id)
        LEFT JOIN delivery_methods dm USING(delivery_method_id)
        LEFT JOIN dispensers d USING(dispenser_id)
        LEFT JOIN states s ON s.state_id=sc.state_id
        WHERE l.launch_id = "{id}"
        """)

    cubesats = cursor.fetchall()
    cubesat_columns = [desc[0] for desc in cursor.description]
    return {
        "columns": columns,
        "rows": rows,
        "cubesat_rows": cubesats,
        "cubesat_columns": cubesat_columns,
    }

@router.get("/rocket_family")
async def get_rocket_family(id: int):
    cursor.execute(f"""
                    SELECT rf.rocket_family_id, rf.name as rocket_family_name, 
                        COUNT(*) as launch_cnt, SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END) as succ_launch_cnt,
                        SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END)/COUNT(*)*100 as succ_rate
                    FROM rocket_families rf
                    LEFT JOIN rockets r USING(rocket_family_id)
                    LEFT JOIN launches l USING(rocket_id)
                    WHERE rf.rocket_family_id = {id}
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                        SELECT ROW_NUMBER() OVER() as row_num, r.name as rocket_name
                        FROM rocket_families rf
                        LEFT JOIN rockets r USING(rocket_family_id)
                        WHERE rf.rocket_family_id = {id}
                        """
                   )

    rocket_rows = cursor.fetchall()
    rocket_columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                        SELECT l.launch_id, datetime(l.launch_at, 'unixepoch') as launch_at, r.name AS rocket_name, 
                            sp.name AS spaceport_name, lp.name AS launchpad_name, 
                            s.state, COUNT(spacecraft_id) AS spacecrafts_cnt
                        FROM launches l
                        LEFT JOIN rockets r USING(rocket_id)
                        LEFT JOIN launchpads lp USING(launchpad_id)
                        LEFT JOIN spaceports sp USING(spaceport_id)
                        LEFT JOIN spacecrafts sc USING(launch_id)
                        LEFT JOIN states s ON s.state_id=l.state_id
                        WHERE r.rocket_family_id = {id}
                        GROUP BY l.launch_id
                        """
                   )

    launch_rows = cursor.fetchall()
    launch_columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                SELECT ROW_NUMBER() OVER() as row_num, sn.name as cubesat_name,
                    scf.name as family_name, datetime(sc.launch_at, 'unixepoch') as launch_at, sp.name AS spaceport_name,
                    lp.name AS launchpad_name, bcs.name as base_cs_name, d.name as container,
                    s.state
                FROM spacecrafts as sc
                LEFT JOIN spacecraft_names sn on sc.primary_name_id=sn.name_id
                LEFT JOIN spacecraft_families scf  USING(family_id)
                LEFT JOIN delivery_methods dm USING(delivery_method_id)
                LEFT JOIN dispensers d USING(dispenser_id)
                LEFT JOIN launches l USING(launch_id)
                LEFT JOIN launchpads lp USING(launchpad_id)
                LEFT JOIN spaceports sp USING(spaceport_id)
                LEFT JOIN base_cs bcs USING(base_spacecraft_id)
                LEFT JOIN states s ON s.state_id=sc.state_id
                WHERE family_id = {id}
                """
                   )

    cubesats = cursor.fetchall()
    cubesat_columns = [desc[0] for desc in cursor.description]

    return {
        "name" : rows[0][0],
        "columns": columns,
        "rows": rows,
        "rocket_rows": rocket_rows,
        "rocket_columns": rocket_columns,
        "launch_rows": launch_rows,
        "launch_columns": launch_columns,
        "cubesat_rows": cubesats,
        "cubesat_columns": cubesat_columns,
    }



@router.get("/spaceport")
async def get_spaceport(id: int):
    cursor.execute(f"""
                    SELECT sp.name as spaceport_name,
                        sp.lat, sp.long,
                        COUNT(*) as launch_cnt, SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END) as succ_launch_cnt,
                        SUM(CASE WHEN l.state_id IS NOT NULL THEN 1 ELSE 0 END)/COUNT(*)*100 as succ_rate
                    FROM spaceports sp
                    LEFT JOIN launchpads lp USING(spaceport_id)
                    LEFT JOIN launches l USING(launchpad_id)
                    WHERE sp.spaceport_id = {id}
                    """
                   )

    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                        SELECT ROW_NUMBER() OVER() as row_num, lp.name as launchpad_name, lp.lat, lp.long, COUNT(*) as launch_cnt
                        FROM spaceports sp
                        LEFT JOIN launchpads lp USING(spaceport_id)
						LEFT JOIN launches l USING(launchpad_id)
                        WHERE sp.spaceport_id = {id}
						GROUP BY lp.launchpad_id
                        """
                   )

    launchpad_rows = cursor.fetchall()
    launchpad_columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                        SELECT l.launch_id, datetime(l.launch_at, 'unixepoch') as launch_at_at, r.name AS rocket_name, 
                            lp.name AS launchpad_name, 
                            s.state, COUNT(spacecraft_id) AS spacecrafts_cnt
                        FROM launches l
                        LEFT JOIN rockets r USING(rocket_id)
                        LEFT JOIN launchpads lp USING(launchpad_id)
                        LEFT JOIN spaceports sp USING(spaceport_id)
                        LEFT JOIN spacecrafts sc USING(launch_id)
                        LEFT JOIN states s ON s.state_id=l.state_id
                        WHERE sp.spaceport_id = {id}
                        GROUP BY l.launch_id
                        """
                   )

    launch_rows = cursor.fetchall()
    launch_columns = [desc[0] for desc in cursor.description]

    cursor.execute(f"""
                SELECT ROW_NUMBER() OVER() as row_num, sn.name as cubesat_name,
                    scf.name as family_name, datetime(sc.launch_at, 'unixepoch') as launch_at_at,
                    lp.name AS launchpad_name, bcs.name as base_cs_name, d.name as container,
                    s.state
                FROM launches l 
                LEFT JOIN spacecrafts as sc USING(launch_id)
                LEFT JOIN spacecraft_names sn on sc.primary_name_id=sn.name_id
                LEFT JOIN spacecraft_families scf  USING(family_id)
                LEFT JOIN delivery_methods dm USING(delivery_method_id)
                LEFT JOIN dispensers d USING(dispenser_id)
                LEFT JOIN launchpads lp USING(launchpad_id)
                LEFT JOIN spaceports sp ON lp.spaceport_id=sp.spaceport_id
                LEFT JOIN base_cs bcs USING(base_spacecraft_id)
                LEFT JOIN states s ON s.state_id=sc.state_id
                WHERE sp.spaceport_id = {id}
                """
                   )

    cubesats = cursor.fetchall()
    cubesat_columns = [desc[0] for desc in cursor.description]

    return {
        "name" : rows[0][0],
        "columns": columns,
        "rows": rows,
        "launchpad_rows": launchpad_rows,
        "launchpad_columns": launchpad_columns,
        "launch_rows": launch_rows,
        "launch_columns": launch_columns,
        "cubesat_rows": cubesats,
        "cubesat_columns": cubesat_columns,
    }



'''



'''
from fastapi.responses import HTMLResponse
import plotly.graph_objects as go
import pandas as pd

ALLOWED_PARAMS = {
    "altitude",
    "inclination",
    "eccentricity",
    "semi_major_axis",
    "perigee_altitude",
    "apogee_altitude",
    "period",
    "mean_motion"
}

@router.get("/orbits_plot", response_class=HTMLResponse)
async def plot_orbit(norad_id: int, parameter: str):
    if parameter not in ALLOWED_PARAMS:
        raise HTTPException(status_code=400, detail="Invalid parameter")

    cursor.execute(f"""
        SELECT event_at, {parameter}
        FROM orbital_events
        WHERE norad_id = ?
        ORDER BY event_at
    """, (norad_id,))

    rows = cursor.fetchall()

    if not rows:
        return "<h3>Нет данных</h3>"

    df = pd.DataFrame(rows, columns=["event_at", "value"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["event_at"], y=df["value"], mode="lines", name=parameter))
    fig.update_layout(title=f"{parameter} для NORAD {norad_id}", xaxis_title="Дата", yaxis_title=parameter, height=600)

    return fig.to_html(full_html=False)

'''



'''
from fastapi import Query

ALLOWED_PARAMS = {
    "altitude",
    "inclination",
    "eccentricity",
    "semi_major_axis",
    "perigee_altitude",
    "apogee_altitude",
    "period",
    "mean_motion"
}

@router.get("/orbits")
async def get_orbits(
    norad_id: int = Query(...),
    parameter: str = Query(...)
):
    if parameter not in ALLOWED_PARAMS:
        raise HTTPException(status_code=400, detail="Invalid parameter")

    query = f"""
        SELECT event_at, {parameter}
        FROM orbital_events
        WHERE norad_id = ?
        ORDER BY event_at
    """

    cursor.execute(query, (norad_id,))
    rows = cursor.fetchall()

    if not rows:
        return {"labels": [], "values": []}

    labels = [r[0] for r in rows]
    values = [r[1] for r in rows]

    return {
        "labels": labels,
        "values": values
    }

'''


