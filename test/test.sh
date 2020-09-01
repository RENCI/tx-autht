#!/bin/bash

set -o allexport
source test/env.docker
set +o allexport

docker-compose -f docker-compose.yml -f test/docker-compose.yml up --build -V --exit-code-from tx-autht
