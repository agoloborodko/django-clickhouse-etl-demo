import psycopg2
from time import sleep
import datetime as dt
import os
import pytz

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    dbname=os.environ['POSTGRES_DB'],
    user=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD']
)

script_get_var_init = """
    SELECT var_cur_value::timestamp 
    FROM metadata.dwh_variables 
    WHERE var_name = 'PROTOTYPE_TS'
"""
script_update_meta_hist = """
    INSERT INTO metadata.dwh_variables_hist 
    SELECT var_name, var_cur_value, now()
    FROM metadata.dwh_variables
    WHERE var_name = 'PROTOTYPE_TS'
    ;
"""


def get_script_update_meta(DWH_VAR_CUR_VALUE):
    script_update_meta = f"""
        UPDATE metadata.dwh_variables 
        SET var_cur_value = '{DWH_VAR_CUR_VALUE}'
        WHERE var_name = 'PROTOTYPE_TS'
    """
    return script_update_meta


def get_insert_into(DWH_VAR_INIT_VALUE, DWH_VAR_CUR_VALUE):
    script_insert_into = f"""
        INSERT INTO mart.prototype 
        SELECT 
            evn."time"
        ,	evn.user_id 
        ,	usr.date_joined AS join_date
        ,	COALESCE(usr.registration_date, to_timestamp('0')) AS registration_date
        ,	usr.username AS "name"
        ,	CASE 
                WHEN COALESCE(
                    usr.registration_date, 
                    now() + INTERVAL '1 day'
                    ) < evn."time"
                THEN 0
                ELSE 1
            END				AS is_guest
        ,	evn.target_id 	AS step_id
        ,	evn.action_id 
        FROM stage_prototype.educational_platform_prototypeevent evn 
            JOIN stage_prototype.educational_platform_prototypeuser usr
            ON usr.id = evn.user_id 
        WHERE 
            evn."time" BETWEEN '{DWH_VAR_INIT_VALUE.strftime(format='%Y-%m-%d %H:%M:%S')}'::timestamp 
                        AND '{DWH_VAR_CUR_VALUE.strftime(format='%Y-%m-%d %H:%M:%S')}'::timestamp
        ;
    """
    return script_insert_into


while True:
    cursor = conn.cursor()

    cursor.execute(script_get_var_init)
    DWH_VAR_INIT_VALUE = cursor.fetchone()[0]
    DWH_VAR_CUR_VALUE = dt.datetime.now(tz=pytz.timezone('Europe/Moscow')) - dt.timedelta(seconds=1)

    cursor.execute(get_script_update_meta(DWH_VAR_CUR_VALUE))
    conn.commit()

    cursor.execute(get_insert_into(DWH_VAR_INIT_VALUE, DWH_VAR_CUR_VALUE))
    conn.commit()

    cursor.execute(script_update_meta_hist)
    conn.commit()

    sleep(int(os.environ['PERIOD']))
