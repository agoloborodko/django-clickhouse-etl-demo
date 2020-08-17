FROM library/postgres
RUN apt-get update && apt-get -y install cron
COPY target_database/scripts/cron_elt /etc/cron.d/cron_elt
RUN chmod 0644 /etc/cron.d/cron_elt && \
    chmod 0777 -R /var/log/
COPY target_database/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod -R 0777 /docker-entrypoint-initdb.d/ && \
    groupadd crond-users && \
    usermod -a -G crond-users postgres
