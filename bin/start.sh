#!/bin/bash

set -e

echo "Starting the application..."
echo "Environment: ${ENV:-development}"

# Add your application startup commands here

flask run --port 8080 &

echo "Application started successfully!" 