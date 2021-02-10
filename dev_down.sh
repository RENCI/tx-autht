#!/bin/bash
set -e

set -o allexport
source env.docker
set +o allexport

docker-compose -f docker-compose.yml down
