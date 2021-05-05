[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/tx-autht?style=plastic)](https://hub.docker.com/repository/docker/txscience/tx-autht/builds)

# tx-autht
Generic containerized authentication module to use a ticket server or direct authentication

This is authentication only, will not include role-based authorization (authz, and/or RBAC)

Not tied to CILogon or Auth0, but can be upgraded to use those technologies.

Please use OpenAuth 2.0 (OAuth2) API as this module's API spec as much as possible.

Leave room for up-grading to federated authentication later, e.g., OpenID Connect
