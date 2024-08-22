#!/bin/bash

# Variables
BACKEND_DIR="backend"
PORT=5000

# Navigate to the backend directory
cd "$BACKEND_DIR"

# Install dependencies
echo "Installing backend dependencies..."
pip install -r requirements.txt

# Start the Flask development server
echo "Starting Flask server on port $PORT..."
export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=$PORT

if [ $? -eq 0 ]; then
    echo "Flask server started successfully!"
else
    echo "Failed to start Flask server!"
    exit 1
fi
