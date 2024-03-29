import os
import json
import requests
from flask import redirect as flask_redirect


def authorize(apikey, provider, return_url, code, redirect):
    server_api_key = os.getenv("API_KEY", "")
    # print("server api key:", server_api_key, ", request api key:", apikey, flush=True)
    if apikey != server_api_key:
        return "Unauthorized", 401
    providers = os.getenv("PROVIDERS", "")
    if not providers:
        return "No provider is supported", 500
    providers = json.loads(providers)
    if provider not in providers.keys():
        return "requested provider is not supported", 500
    auth_url = providers[provider]['AUTH_URL']
    if not code and 'LOGIN_URL' not in providers[provider]:
        return "Fail to authenticate: no token code is provided for the provider", 400
    q_auth_url = f"{auth_url}?code={code}"
    r = requests.get(q_auth_url)
    if return_url.endswith('/'):
        return_url = return_url[:-1]
    if r.status_code == 200:
        r_json = r.json()
        # print(r_json, flush=True)
        if redirect:
            key_val_str = ''
            for key, val in r.json().items():
                key_val_str = f"{key_val_str}&{key}={val}"
            redirect_url = f"{return_url}?status=success{key_val_str}"
            #return redirect_url, 200
            return flask_redirect(redirect_url)
        else:
            return r_json
    else:
        r_json = {'content': str(r.content),
                  'status_code': r.status_code}
        # print(r_json, flush=True)
        if redirect:
            # print(r.status_code, r.content, flush=True)
            status_code = r.status_code
            redirect_url = f"{return_url}?status=failure&status_code={status_code}"
            # return redirect_url, status_code
            return flask_redirect(redirect_url)
        else:
            return r_json, r.status_code
