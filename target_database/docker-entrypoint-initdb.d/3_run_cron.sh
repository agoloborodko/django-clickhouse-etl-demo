#!/usr/bin/env bash

crontab /home/elt/cron_elt
touch /var/log/cron.log
cron && tail -f /var/log/cron.log
