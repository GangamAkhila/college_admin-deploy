#!/bin/bash
# build_files.sh

echo "Building project..."

# Install dependencies
python3 -m pip install -r requirements.txt

# Run migrations
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "Build completed."
