#!/usr/bin/env bash

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} << EOF
CREATE EXTENSION IF NOT EXISTS postgres_fdw;

CREATE SERVER IF NOT EXISTS prototype_server 
	FOREIGN DATA WRAPPER postgres_fdw
	OPTIONS (
		host 'pg_database', 
		dbname ${FOREIGN_DB}, 
		port '5432'
);

CREATE USER MAPPING IF NOT EXISTS FOR db_user 
	SERVER prototype_server
	OPTIONS (
		USER ${FOREIGN_USER},
		PASSWORD ${FOREIGN_PASS}
	);


CREATE SCHEMA IF NOT EXISTS stage_prototype; 

IMPORT FOREIGN SCHEMA public
	FROM SERVER prototype_server
	INTO stage_prototype
;
EOF