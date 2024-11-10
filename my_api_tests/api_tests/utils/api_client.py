import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, handle, method="GET", json=None):
        url = f"{self.base_url}{handle}"
        response = requests.request(method=method, url=url, json=json)
        return response

client = APIClient(base_url="http://127.0.0.1:8000")
