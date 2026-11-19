#!/usr/bin/env bash
# Prepara y levanta Airflow con Docker Compose (compose oficial 3.4.0).
set -euo pipefail

VERSION_COMPOSE="3.4.0"
URL="https://airflow.apache.org/docs/apache-airflow/${VERSION_COMPOSE}/docker-compose.yaml"

cd "$(dirname "$0")"
if [ ! -f docker-compose.yaml ]; then
  curl -LfO "$URL"
fi
mkdir -p ./dags ./logs ./plugins ./config
if [ ! -f .env ]; then
  echo "AIRFLOW_UID=50000" > .env
fi
docker compose up airflow-init
docker compose up -d
echo "Airflow arrancando. Abre el puerto 8080 (usuario y contraseña: airflow)."
