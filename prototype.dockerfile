FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN mkdir -p /home/hyperskill_prototype
WORKDIR /home/hyperskill_prototype
COPY hyperskill_prototype/ .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod -R 0777 .

ENTRYPOINT ["/home/hyperskill_prototype/entrypoint.sh"]
