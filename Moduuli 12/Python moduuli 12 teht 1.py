import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random")
json_response = response.json()
result = json_response["value"]
print(result)