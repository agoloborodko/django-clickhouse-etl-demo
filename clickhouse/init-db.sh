#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE docker;
    CREATE TABLE docker.docker (x Int32) ENGINE = Log;
    CREATE USER docker_admin IDENTIFIED BY 'pass';
    GRANT ALL ON docker TO docker_admin WITH GRANT OPTION;
EOSQL
