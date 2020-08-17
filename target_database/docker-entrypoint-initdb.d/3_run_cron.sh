#!/usr/bin/env bash

crontab /home/elt/cron_elt
cron && tail -f /var/log/cron.log
