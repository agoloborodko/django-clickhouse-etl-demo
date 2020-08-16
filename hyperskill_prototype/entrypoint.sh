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
echo "from educational_platform.models import PrototypeUser; PrototypeUser.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
