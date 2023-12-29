#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations djangoapp
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
py rundev 0.0.0.0:8000