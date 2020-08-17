#!/usr/bin/env bash

# Start the run once job.
echo "Scheduling ELT process"

# Setup a cron schedule
echo "5 * * * * /elt.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f
