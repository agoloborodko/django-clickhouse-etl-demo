DO
$$
DECLARE 
	DWH_VAR_INIT_VALUE timestamp := '1970-01-01';
	DWH_VAR_CUR_VALUE timestamp := '1970-01-01';
BEGIN
	SELECT var_cur_value::timestamp INTO DWH_VAR_INIT_VALUE FROM metadata.dwh_variables
	;
	
	UPDATE metadata.dwh_variables 
	SET var_cur_value = now() - INTERVAL '1 second'
	WHERE var_name = 'PROTOTYPE_TS'
	;
	
	SELECT var_cur_value::timestamp INTO DWH_VAR_CUR_VALUE FROM metadata.dwh_variables
	;
	
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
		evn."time" BETWEEN DWH_VAR_INIT_VALUE AND DWH_VAR_CUR_VALUE
	;
	
	INSERT INTO metadata.dwh_variables_hist 
	SELECT var_name, var_cur_value, now()
	FROM metadata.dwh_variables
	WHERE var_name = 'PROTOTYPE_TS'
	;
	
	COMMIT
	;

END;
$$ LANGUAGE plpgsql;