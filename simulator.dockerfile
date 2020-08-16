FROM locustio/locust

USER root
RUN apt-get update && apt-get install -y netcat

COPY hyperskill_simulator/ .
RUN chmod 0777 .

USER locust

ENTRYPOINT ["entrypoint.sh"]
