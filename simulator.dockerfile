FROM locustio/locust

USER root
COPY hyperskill_simulator/ .
RUN chmod -R 0777 .
USER locust

ENTRYPOINT ["/home/locust/entrypoint.sh"]
