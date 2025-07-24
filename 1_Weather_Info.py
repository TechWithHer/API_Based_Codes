#Check weather by city name
#OpenWeatherMap API	

import requests

API_KEY= "a6e434a67819305d638a3ce277962a71"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]
        print(f"\n📍 City: {data['name']}")
        print(f"🌡️ Temperature: {main['temp']}°C")
        print(f"💧 Humidity: {main['humidity']}%")
        print(f"🌤️ Condition: {weather['description'].capitalize()}")
    else:
        print("❌ Failed to get weather data. Check the city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)    