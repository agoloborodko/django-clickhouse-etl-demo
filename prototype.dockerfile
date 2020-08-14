FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /hyperskill_prototype
WORKDIR /hyperskill_prototype
COPY hyperskill_prototype/ /hyperskill_prototype/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations educational_platform
RUN python manage.py migrate
RUN python manage.py runserver
