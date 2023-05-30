# Weather_Forcasting
A command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python.
To use this code:

Replace "YOUR_API_KEY" in the url variable with your actual OpenWeatherMap API key. You can sign up for a free API key at https://openweathermap.org/.

Save the code to a Python file, e.g., weather_forecast.py.

Open a terminal or command prompt, navigate to the directory where the file is saved, and execute the script by running python weather_forecast.py.

Enter the name of the city for which you want to retrieve the weather forecast.

The script will make a request to the OpenWeatherMap API, retrieve the weather data for the specified city, and display the weather, temperature, and humidity information. It includes error handling to handle cases where the API request fails or encounters an exception.

Please note that you need to have the requests library installed in your Python environment. You can install it by running pip install requests in your terminal or command prompt.
