#!/bin/bash
set -e

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "Database is ready!"

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Create default data if needed
echo "Setting up initial data..."
python -c "
from app import engine, Base
Base.metadata.create_all(bind=engine)
print('Database tables created')
"

# Start the application
echo "Starting {{ app_name }}..."
exec "$@"
