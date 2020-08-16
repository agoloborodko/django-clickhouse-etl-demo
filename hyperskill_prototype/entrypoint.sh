#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT
do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py flush --no-input
python manage.py makemigrations educational_platform
python manage.py migrate
echo "from educational_platform.models import PrototypeUser; PrototypeUser.objects.create_superuser('${SUPERUSER_NAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASS}')" | python manage.py shell
echo "from educational_platform.models import PrototypeTask; PrototypeTask.objects.bulk_create([PrototypeTask()]*5)" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
