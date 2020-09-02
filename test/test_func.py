import requests


def test_authorize():
    resp = requests.get("http://tx-autht:8080/authorize?apikey=TEST123&provider=venderbilt&code=testAuth1234&return_url=http://tx-autht:8080")
    assert resp.status_code == 200
