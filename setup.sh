#!/bin/bash
echo "Starting College Management System Setup..."

# Step 1: Create Virtual Environment
echo "Creating virtual environment..."
python -m venv venv

# Step 2: Activate Virtual Environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install Requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Run Migrations
echo "Running database migrations..."
python manage.py makemigrations app1
python manage.py migrate

# Step 5: Create Superuser
echo "Creating superuser (admin:admin123)..."
export DJANGO_SUPERUSER_PASSWORD=admin123
python manage.py createsuperuser --noinput --username admin --email admin@admin.com

# Step 6: Start Server
echo "Starting development server..."
python manage.py runserver
