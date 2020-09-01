import requests

json_headers = {
    "Accept": "application/json"
}

json_post_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def test_ui():
    resp = requests.get("http://tx-autht:8080/ui")

    assert resp.status_code == 200
