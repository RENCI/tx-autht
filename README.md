[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/txautht?style=plastic)](https://hub.docker.com/repository/docker/txscience/txautht/builds)

# tx-autht
Generic containerized authentication module to use a ticket server or direct authentication

This is authentication only, will not include role-based authorization (authz, and/or RBAC)

Not tied to CILogon or Auth0, but can be upgraded to use those technologies.

Please use OpenAuth 2.0 (OAuth2) API as this module's API spec as much as possible.

Leave room for up-grading to federated authentication later, e.g., OpenID Connect

## Deploy and restart the service
- ssh to the VM
- ```sudo su - auth```
- ```cd /var/opt/auth_service/tx-autht```
- Run ``./prod_up.sh``` to start the service for the first time or run ```./prod_down.sh``` first to bring down containers followed by ```prod_up.sh``` to restart the service.
