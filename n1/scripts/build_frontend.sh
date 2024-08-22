#!/bin/bash

# Variables
FRONTEND_DIR="frontend"
BUILD_DIR="dist"

# Navigate to the frontend directory
cd "$FRONTEND_DIR"

# Install dependencies and build the frontend
echo "Building Vue.js frontend..."
npm install
npm run build

if [ $? -eq 0 ]; then
    echo "Frontend build successful!"
else
    echo "Frontend build failed!"
    exit 1
fi

# Move the build output to a deployment directory if needed
# cp -r "$BUILD_DIR" ../deploy_directory/
