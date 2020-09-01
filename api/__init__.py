import os
import requests
import connexion
from flask import redirect


def authorize(provider, return_url, code):
    api_key = connexion.request.headers['X-API-KEY']
    server_api_key = os.getenv("API_KEY", "")
    if api_key != server_api_key:
        return "Unauthorized", 401
    providers = os.getenv("PROVIDERS", "")
    if not providers:
        return "No provider is supported", 500
    if provider not in providers.keys():
        return "requested provider is not supported", 500
    auth_url = providers[provider]['AUTH_URL']
    if not code and 'LOGIN_URL' not in providers[provider]:
        return "Fail to authenticate: no token code is provided for the provider", 400
    q_auth_url = f"{auth_url}?code={code}"
    r = requests.get(q_auth_url)
    return redirect(return_url, code=302, response=r)
