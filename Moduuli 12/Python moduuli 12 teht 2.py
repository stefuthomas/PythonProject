import requests
import json

user_input = str(input("Kohde: "))
request = (f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=be35bc47b601dbd0fb77cf603fdd5460&units=metric")

try:
      response = requests.get(request)
      if response.status_code==200:
            json_response = response.json()
            result = json_response
            print(f"{result['name']}:\n"
                  f"Sää: {result['weather'][0]['description']}\n"
                  f"Lämpötila: {result['main']['temp']} °C")
except requests.exceptions.RequestException as e:
      print ("Hakua ei voitu suorittaa.")