#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE IF NOT EXISTS prototype_dwh;
    CREATE USER IF NOT EXISTS prototype_admin IDENTIFIED BY 'pass';
    ALTER USER default SETTINGS allow_introspection_functions=1;
    GRANT ALL ON *.* TO prototype_admin WITH GRANT OPTION;
    ALTER USER default SETTINGS allow_introspection_functions=0;
EOSQL
