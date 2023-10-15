import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
    else:
        print("City not found or an error occurred.")

city = input("Enter city name: ")
get_weather(city)
