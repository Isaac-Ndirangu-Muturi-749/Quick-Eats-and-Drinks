#!/bin/bash

# Variables
BACKEND_DIR="backend"
PORT=8000

# Navigate to the backend directory
cd "$BACKEND_DIR"

# Install dependencies
echo "Installing backend dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Start the Django development server
echo "Starting Django server on port $PORT..."
python manage.py runserver 0.0.0.0:$PORT

if [ $? -eq 0 ]; then
    echo "Django server started successfully!"
else
    echo "Failed to start Django server!"
    exit 1
fi
