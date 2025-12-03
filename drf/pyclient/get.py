import requests

endpoint = "http://localhost:8080/api/products/get/3"  # abc=123 is also a query parameter
response = requests.get(endpoint, params={"ltr":123}) # params means query parameters

print(response.text)