FROM library/postgres
RUN apt-get update && apt-get -y install cron && \
    mkdir /home/elt/
COPY target_database/scripts/cron_elt /home/elt/cron_elt
COPY target_database/scripts/cron_elt /etc/cron.d/cron_elt
RUN chmod 0644 -R /etc/cron.d/ && \
    chmod 0777 -R /var/log/ && \
    chmod 0777 -R /var/run/ && \
    chmod 0777 -R /home/elt/
COPY target_database/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod -R 0777 /docker-entrypoint-initdb.d/ && \
    groupadd crond-users && \
    usermod -a -G crond-users postgres
