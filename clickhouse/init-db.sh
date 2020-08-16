#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE prototype_dwh;
    CREATE USER prototype_admin IDENTIFIED BY 'pass';
    GRANT ALL ON prototype_dwh TO prototype_admin WITH GRANT OPTION;
EOSQL
#    CREATE TABLE docker.docker (x Int32) ENGINE = Log;
