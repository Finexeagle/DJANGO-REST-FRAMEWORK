import requests

endpoint = "http://localhost:8080/api/products/get/1"  # abc=123 is also a query parameter
response = requests.get(endpoint, params={"ltr":123}, json={"title":"From client"}) # params means query parameters

print(response.text)