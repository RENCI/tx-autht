#!/bin/bash

set -o allexport
source env.docker
set +o allexport

docker-compose -f docker-compose.yml -f test/docker-compose.yml up --build -V --exit-code-from tx-autht
