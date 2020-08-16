FROM locustio/locust
RUN mkdir -p /home/hyperskill_simulator
WORKDIR /home/hyperskill_simulator
COPY hyperskill_simulator/ .

RUN chmod -R 0777 .

RUN locust