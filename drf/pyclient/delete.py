import requests

endpoint = "http://localhost:8080/api/products/delete/2"  # abc=123 is also a query parameter
response = requests.delete(endpoint) # params means query parameters

print(response.text)