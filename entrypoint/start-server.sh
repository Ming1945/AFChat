#!/bin/bash

echo "🔥 Initialising the app..."
python3 -m pip install -r requirements.txt
echo "🔥 Collecting static files..."
python manage.py collectstatic --no-input
echo "🔥 Migrating database..."
python manage.py makemigrations
python manage.py migrate --no-input
echo "🔥 Removing stale content types..."
python manage.py remove_stale_contenttypes --no-input
echo "🔥 Copying static files..."
cp -r static/* static/
echo "✅ Initialisation is done."

nginx

exec $@