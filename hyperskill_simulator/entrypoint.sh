#!/bin/sh

sleep 5
echo "Waiting for prototype..."
sleep 5
echo "assume prototype started"
locust --headless --host http://$HOST:$PORT -u $USERS_NUM -r $HATCH_RATE
