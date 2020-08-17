#!/usr/bin/env bash

crontab /etc/cron.d/cron_elt
touch /var/log/cron.log
cron && tail -f /var/log/cron.log
