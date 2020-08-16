FROM locustio/locust
COPY hyperskill_simulator/ .
ENTRYPOINT ["locust --config=locust.conf"]
