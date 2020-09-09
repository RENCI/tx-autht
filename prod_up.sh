#!/bin/bash
docker-compose -f docker-compose.yml -f nginx/docker-compose.yml up --build -V -d