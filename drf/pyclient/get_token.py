import requests
from getpass import getpass

password = getpass()

endpoint = "http://localhost:8080/api/auth/"
auth_response = requests.post(endpoint, json={'username': 'mrx', 'password': password})

try:
    print(auth_response.json())
except:
    print(auth_response.status_code)

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8080/api/products/get/3"
    response = requests.get(endpoint, headers=headers)
    print(response.text)

