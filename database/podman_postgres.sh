#!/bin/bash
podman run -d --name postgres \
  -e POSTGRES_PASSWORD=socialmedia \
  -e POSTGRES_DB=socialmedia \
  -p 5433:5432 \
  -v social_media_analysis_pgdata:/var/lib/postgresql/data \
  postgres
