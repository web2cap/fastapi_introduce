#!/bin/bash
docker compose down
docker container rm booking_infra-booking_celery
docker container rm booking_infra-booking_flower
docker container rm booking_infra-booking_back
docker volume rm booking_infra_grafanadata
docker volume rm booking_infra_prometheusdata
docker compose up