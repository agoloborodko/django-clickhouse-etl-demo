FROM yandex/clickhouse-server

COPY clickhouse/config.xml /etc/clickhouse-server/config.xml
COPY clickhouse/users.xml /etc/clickhouse-server/users.xml
COPY clickhouse/init-db.sh /docker-entrypoint-initdb.d

ENTRYPOINT ["/entrypoint.sh"]