FROM library/postgres
COPY /target_database/. /docker-entrypoint-initdb.d/
