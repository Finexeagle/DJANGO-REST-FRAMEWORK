import requests

endpoint = "http://localhost:8000/api/"  # abc=123 is also a query parameter
response = requests.get(endpoint, params={"ltr":123}) # params means query parameters

print(response.text)