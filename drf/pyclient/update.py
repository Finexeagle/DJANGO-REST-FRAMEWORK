import requests

endpoint = "http://localhost:8080/api/products/update/2"  # abc=123 is also a query parameter

data = {
  "title":"Updated"
}
response = requests.patch(endpoint, params={"ltr":123}, json=data) # params means query parameters

print(response.text)