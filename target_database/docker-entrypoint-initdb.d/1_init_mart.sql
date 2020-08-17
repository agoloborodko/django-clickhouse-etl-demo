CREATE SCHEMA IF NOT EXISTS mart;

CREATE TABLE mart.prototype(
	"time" Timestamp
,	user_id int
,	join_date timestamp
,	registration_date timestamp
,	"name" varchar(255)
,	is_guest smallint
,	step_id int
,	action_id smallint
);

