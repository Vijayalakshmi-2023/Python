import requests
import json
import time
from datetime import datetime

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.favorites = []

    # Fetch current weather by location
    def get_current_weather(self, location, units="metric"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units={units}&appid={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather = {
                "location": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            }
            return weather
        else:
            print("Error: Could not retrieve weather data.")
            return None

    # Get 5-day weather forecast
    def get_5_day_forecast(self, location, units="metric"):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&units={units}&appid={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            forecast = []
            for entry in data["list"]:
                forecast.append({
                    "date": datetime.fromtimestamp(entry["dt"]).strftime('%Y-%m-%d %H:%M:%S'),
                    "temperature": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"],
                    "humidity": entry["main"]["humidity"],
                    "wind_speed": entry["wind"]["speed"]
                })
            return forecast
        else:
            print("Error: Could not retrieve forecast data.")
            return None

    # Convert temperature unit
    def convert_temperature(self, temp, from_unit, to_unit):
        if from_unit == "metric" and to_unit == "imperial":
            return (temp * 9/5) + 32
        elif from_unit == "imperial" and to_unit == "metric":
            return (temp - 32) * 5/9
        elif from_unit == "metric" and to_unit == "kelvin":
            return temp + 273.15
        elif from_unit == "kelvin" and to_unit == "metric":
            return temp - 273.15
        elif from_unit == "imperial" and to_unit == "kelvin":
            return (temp - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "imperial":
            return (temp - 273.15) * 9/5 + 32
        return temp

    # Display current weather
    def display_current_weather(self, location, units="metric"):
        weather = self.get_current_weather(location, units)
        if weather:
            print(f"Current Weather in {weather['location']} ({weather['timestamp']}):")
            print(f"Temperature: {weather['temperature']}°")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Pressure: {weather['pressure']} hPa")
            print(f"Wind Speed: {weather['wind_speed']} m/s")
        print("\n")

    # Display 5-day forecast
    def display_5_day_forecast(self, location, units="metric"):
        forecast = self.get_5_day_forecast(location, units)
        if forecast:
            print(f"5-Day Forecast for {location}:")
            for day in forecast:
                print(f"{day['date']} - Temp: {day['temperature']}° | {day['description']} | Humidity: {day['humidity']}% | Wind Speed: {day['wind_speed']} m/s")
        print("\n")

    # Add a location to favorites
    def add_favorite(self, location):
        if location not in self.favorites:
            self.favorites.append(location)
            print(f"Location '{location}' added to favorites.")
        else:
            print(f"Location '{location}' is already in favorites.")

    # View all favorite locations
    def view_favorites(self):
        if self.favorites:
            print("Favorite Locations:")
            for location in self.favorites:
                print(location)
        else:
            print("No favorite locations added.")

    # Weather alerts (for now, just a basic notification about severe weather conditions)
    def weather_alerts(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            alerts = data.get('alerts', None)
            if alerts:
                print("Weather Alerts:")
                for alert in alerts:
                    print(f"{alert['event']} from {alert['start']} to {alert['end']}")
            else:
                print("No weather alerts at the moment.")
        else:
            print("Error: Could not retrieve weather alerts.")
    
    # Main interface for the user
    def main(self):
        while True:
            print("\n=== Weather App ===")
            print("1. Get Current Weather")
            print("2. Get 5-Day Forecast")
            print("3. Add Location to Favorites")
            print("4. View Favorite Locations")
            print("5. View Weather Alerts")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                location = input("Enter the location: ")
                units = input("Choose temperature units (metric/imperial/kelvin): ").lower()
                self.display_current_weather(location, units)
            
            elif choice == '2':
                location = input("Enter the location: ")
                units = input("Choose temperature units (metric/imperial/kelvin): ").lower()
                self.display_5_day_forecast(location, units)

            elif choice == '3':
                location = input("Enter the location to add to favorites: ")
                self.add_favorite(location)

            elif choice == '4':
                self.view_favorites()

            elif choice == '5':
                location = input("Enter the location for weather alerts: ")
                self.weather_alerts(location)

            elif choice == '6':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    weather_app = WeatherApp(api_key)
    weather_app.main()
