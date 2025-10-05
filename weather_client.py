import requests

def get_weather(city):
    api_key = "5452f72200cb738aa051bda174ee5242"  # 🔑 Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        print(f"\n🌤 Weather Report for {city.capitalize()} 🌤")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError:
        print("❌ City not found or invalid request.")
    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
