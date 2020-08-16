#Не забыть:
**docker-compose:**

*Задокументировать environment variables* 

database:
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB

prototype:
- DB_USER=db_user
- DB_PASS=db_pass
- DB_NAME=prototype_database
- DB_HOST=database
- DB_PORT=5432

*Задокументировать отсутствие volumes*

**hyperskill_prototype:**
1) pip install -r requirements.txt
   
   pip install --upgrade pip
2) manage.py makemigrations educational_platform
3) python manage.py migrate
4) python manage.py createsuperuser
5) python manage.py runserver
6) для superuser должна быть настройка логина и пароля в докерфайле
7) django secret key надо куда-то убрать

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

https://stackoverflow.com/questions/57873434/dockerdjangosecret-key-regenerate

dd if=/dev/urandom bs=60 count=1 | base64


**hyperskill_simulator:**
1) pip install -r requirements.txt
2) https://www.blazemeter.com/blog/how-to-run-locust-with-different-users
3) https://docs.locust.io/en/stable/quickstart.html