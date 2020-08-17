FROM python:3
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"

RUN mkdir -p /home/etl
WORKDIR /home/etl
COPY etl/ .

RUN apt-get update && apt-get install -y netcat && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod -R 0777 .

ENTRYPOINT ["/home/etl/entrypoint.sh"]
