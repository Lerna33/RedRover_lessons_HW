def log_response(response):
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
