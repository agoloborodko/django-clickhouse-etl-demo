# django-clickhouse-etl-demo

##Установка и запуск
```bash
git clone https://github.com/agoloborodko/django-clickhouse-etl-demo.git
cd django-clickhouse-etl-demo
docker-compose up
```

После запуска приложение, целевая база данных и симуляция пользователей запустятся автоматически

##Доступ к Django-приложению
Приложение доступно по адесу `localhost:2999`
Оно позволяет добавлять тестовых пользователей, просматривать задачи и отправлять "решения"

##Доступ к БД
Итоговая база данных доступна со следующими параметрами:

* Тип БД: PostgreSQL
* Порт: 1020
* Название БД: prototype_dwh
* Имя пользователя: db_user
* Пароль: db_pass

##Прочие настройки
Все настройки находятся в файле docker-compose.yml
