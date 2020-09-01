import requests


def test_authorize():
    headers = {
        'X-API-Key': "Test123"
    }
    resp = requests.get("http://tx-autht:8080/authorize?provider=venderbilt&code=testAuth1234&return_url=http://tx-autht:8080",
                        headers=headers)
    assert resp.status_code == 200
