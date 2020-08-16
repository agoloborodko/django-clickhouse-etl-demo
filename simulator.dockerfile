FROM locustio/locust

RUN apt-get update && apt-get install -y netcat

COPY hyperskill_simulator/ .
RUN chmod 0777 entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
