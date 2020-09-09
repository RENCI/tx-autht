import requests


def test_authorize():
    # test apikey authorization
    resp = requests.get("http://txautht:8080/authorize?apikey=wrongkey&provider=venderbilt&code=testAuth1234&return_url=http://tx-autht:8080")
    assert resp.status_code == 401
    # test provider parameter
    resp = requests.get("http://txautht:8080/authorize?apikey=TEST123&code=testAuth1234&return_url=http://tx-autht:8080")
    assert resp.status_code == 500
    # test not supported provider parameter
    resp = requests.get("http://txautht:8080/authorize?apikey=TEST123&provider=doesnotexist&code=testAuth1234&return_url=http://tx-autht:8080")
    assert resp.status_code == 500
    # test a valid code has to be provided for venderbilt provider user authentication
    resp = requests.get("http://txautht:8080/authorize?apikey=TEST123&provider=venderbilt&return_url=http://tx-autht:8080")
    assert resp.status_code == 400
    resp = requests.get("http://txautht:8080/authorize?apikey=TEST123&provider=venderbilt&code=notvalidcode&return_url=http://tx-autht:8080")
    assert resp.status_code != 200
    # test a valid code for venderbilt provider succeeds in user authentication
    resp = requests.get("http://txautht:8080/authorize?apikey=TEST123&provider=venderbilt&code=testAuth1234&return_url=http://tx-autht:8080")
    assert resp.status_code == 200
