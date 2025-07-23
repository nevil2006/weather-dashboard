# weather_api.py
import requests

API_KEY = "4445863f36712e807804d4aa9d53e1df"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "main": data["weather"][0]["main"]
        }
    else:
        return None
