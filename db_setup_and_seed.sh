#!/usr/bin/env bash

# Remove existing migrations folder and database file
echo "Removing migrations folder and database file..."
sudo rm -rf ./migrations/
sudo rm -f ./instance/site.db

# Initialize the migration repository
echo "Initializing database migrations..."
flask db init

# Generate an initial migration script
echo "Generating migration script..."
flask db migrate -m "Initial migration."

# Apply the migration to the database
echo "Applying migration..."
flask db upgrade

# Create the admin user
echo "Creating admin user..."
python create_admin.py

# Seed the database with initial data
echo "Seeding database..."
python seed.py

echo "Script completed successfully!"
