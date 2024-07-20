import requests

def fetch_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

print("\t\tWelcome to the Weather Forecaster!\n")
city_name = input("Enter the name of the city: ").strip()
api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
fetch_weather(city_name, api_key)
