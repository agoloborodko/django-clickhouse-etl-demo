CREATE SCHEMA IF NOT EXISTS metadata;

CREATE TABLE IF NOT EXISTS metadata.dwh_variables(
	var_name Varchar(100)
,	var_type Varchar(100)
,	var_init_value Varchar(500)
,	var_cur_value Varchar(500)
,	var_expression varchar(50000)
,	CONSTRAINT PK_dwh_variables PRIMARY KEY (var_name)
);


CREATE TABLE IF NOT EXISTS metadata.dwh_variables_hist(
	var_name varchar(100)
,	var_cur_value varchar(500)
,	refresh_ts timestamp
,	CONSTRAINT PK_dwh_variables_hist PRIMARY KEY (var_name, refresh_ts)
);

INSERT INTO metadata.dwh_variables
VALUES(
    'PROTOTYPE_TS'
,   'Timestamp'
,   '1970-01-01'
,   '1970-01-01'
,   now() - INTERVAL '1 second'
);
