FROM library/postgres
COPY target_database/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod -R 0755 /docker-entrypoint-initdb.d/
