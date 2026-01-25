#!/bin/bash

# Wait for database (optional but good for stability)
sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist (using custom command)
echo "Ensuring superuser exists..."
python manage.py create_superuser

# Build Tailwind assets
echo "Building Tailwind assets..."
python manage.py tailwind build

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3 --timeout 120
