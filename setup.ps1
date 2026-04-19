Write-Host "Starting College Management System Setup..." -ForegroundColor Cyan

# Step 1: Create Virtual Environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Step 2: Activate Virtual Environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\activate

# Step 3: Install Requirements
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Step 4: Run Migrations
Write-Host "Running database migrations..." -ForegroundColor Yellow
python manage.py makemigrations app1
python manage.py migrate

# Step 5: Create Superuser
Write-Host "Creating superuser (admin:admin123)..." -ForegroundColor Yellow
$env:DJANGO_SUPERUSER_PASSWORD="admin123"
python manage.py createsuperuser --noinput --username admin --email admin@admin.com

# Step 6: Start Server
Write-Host "Starting development server..." -ForegroundColor Green
python manage.py runserver
