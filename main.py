import requests
import json


def get_weather_forecast(city):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0325388298bc5457a9f303e3c647c056"

    try:
        response = requests.get(url)
        data = response.json()

        # hi i have added to this code .
        # welcome to weather forecasting.

        # Check if the API response was successful
        if response.status_code == 200:
            # Extract relevant information from the response
            weather = data['weather'][0]['main']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            # Print the weather forecast
            print(f"Weather forecast for {city}:")
            print(f"Weather: {weather}")
            print(f"Temperature: {temperature} K")
            print(f"Humidity: {humidity}%")
        else:
            print("Error occurred while fetching weather data. Please try again.")
# here is an f string implementation
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather_forecast(city)
