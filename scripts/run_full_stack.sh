#!/usr/bin/env bash
set -e
docker compose -f serving/compose.full.yaml up -d --build
echo "Waiting 8s for services..."
sleep 8
echo "MinIO:   http://localhost:9001  (user: ${MINIO_ROOT_USER:-minioadmin})"
echo "MLflow:  http://localhost:5000"
echo "API:     http://localhost:8000/docs"
