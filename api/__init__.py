import os
import requests
import webbrowser
import connexion


def authorize(provider, return_url):
    api_key = connexion.request.headers['X-API-KEY']
    server_api_key = os.getenv("API_KEY", "")
    if api_key != server_api_key:
        return "Unauthorized", 401
    providers = os.getenv("PROVIDERS", "")
    if not providers:
        return "No provider is supported", 500
    if provider not in providers.keys():
        return "requested provider is not supported", 500
    login_url = providers[provider]['LOGIN_URL']
    webbrowser.open(login_url)
    
    auth_url = providers[provider]['AUTH_URL']
    if return_url.endswith('/'):
        aug_return_url = f"{return_url}success"
    else:
        aug_return_url = f"{return_url}/success"
    webbrowser.open(aug_return_url)
    return {}
