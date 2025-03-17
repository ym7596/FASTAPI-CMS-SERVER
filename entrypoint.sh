#!/bin/bash

set -e

echo "Waiting for database to be ready..."

source /src/.venv/bin/activate
sleep 10

echo "Start Server"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000