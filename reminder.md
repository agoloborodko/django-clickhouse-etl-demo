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

*Задокументировать порты и имена контейнеров*

**hyperskill_prototype:**
1) python manage.py createsuperuser
2) для superuser должна быть настройка логина и пароля в докерфайле
3) Задокументировать ALLOWED_HOSTS = ['*']


**hyperskill_simulator:**
1) pip install -r requirements.txt
2) https://www.blazemeter.com/blog/how-to-run-locust-with-different-users
3) https://docs.locust.io/en/stable/quickstart.html