#!/bin/sh

echo "Waiting for dwh..."

while ! nc -z $DB_HOST $DB_PORT
do
  sleep 0.1
done

echo "dwh started"

python etl.py