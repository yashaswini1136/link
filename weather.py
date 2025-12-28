import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Details")
    print("----------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"Condition: {condition}")

else:
    print("City not found or API error.")
