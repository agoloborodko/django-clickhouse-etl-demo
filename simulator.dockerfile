FROM locustio/locust
COPY hyperskill_simulator/ .
ENTRYPOINT ["locust"]
