#!/bin/bash

set -e

docker compose -f meters.docker-compose.yml down
docker compose -f docker-compose.yml up -d --build
docker compose -f docker-compose.yml run db-mgmt /bin/python3 /clear_smartmeter.py
docker compose -f meters.docker-compose.yml up -d --build
echo "Waiting 15s for meters to register..."
sleep 15
docker compose -f docker-compose.yml run db-mgmt /bin/python3 /assign_smartmeters.py
