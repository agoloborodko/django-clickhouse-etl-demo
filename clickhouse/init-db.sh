#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE prototype_dwh;
    CREATE USER prototype_admin IDENTIFIED BY 'pass';
    ALTER USER prototype_admin SETTINGS allow_introspection_functions=1
    GRANT ALL ON *.* TO prototype_admin WITH GRANT OPTION;
EOSQL
