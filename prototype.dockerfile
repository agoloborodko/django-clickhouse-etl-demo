FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /hyperskill_prototype
WORKDIR /hyperskill_prototype
COPY hyperskill_prototype/ /hyperskill_prototype/
RUN pip install -r requirements.txt

ENTRYPOINT ["hyperskill_prototype/entrypoint.sh"]
