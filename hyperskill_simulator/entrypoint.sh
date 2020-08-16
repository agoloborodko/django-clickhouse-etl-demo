#!/bin/sh

echo "Waiting for prototype..."

while ! nc -z $HOST $PORT
do
  sleep 0.1
done

echo "prototype started"

locust --headless --host $HOST --web-port $PORT -u $USERS_NUM -r $HATCH_RATE
