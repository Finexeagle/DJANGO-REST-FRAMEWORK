import requests

endpoint = "http://localhost:8080/api/products/list/"  # abc=123 is also a query parameter
response = requests.get(endpoint) # params means query parameters

print(response.text)