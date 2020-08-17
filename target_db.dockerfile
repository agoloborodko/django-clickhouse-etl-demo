FROM library/postgres
COPY target_database/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod -R 0777 /docker-entrypoint-initdb.d/ && \
    groupadd crond-users && \
    chgrp crond-users /var/run/crond.pid && \
    usermod -a -G crond-users postgres && \
    usermod -a -G crond-users db_user
