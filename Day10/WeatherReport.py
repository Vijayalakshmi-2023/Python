# Structure: {city_name: [temps]}
weather_data = {
    "Chennai": [22, 24, 21, 19, 25],
    "Delhi": [28, 30, 32, 29, 31],
    "Mumbai": [18, 20, 22, 19, 21],
    "Madurai": [30, 31, 33, 34, 32]
}

# Add a new temperature for a specific city
def add_temperature(city_name, temp):
    if city_name in weather_data:
        weather_data[city_name].append(temp)
        print(f"Added {temp}° to {city_name}.")
    else:
        print(f"{city_name} is not in the records.")
        
# Calculate the average temperature for a city
def calculate_avg_temperature(city_name):
    if city_name in weather_data:
        avg_temp = sum(weather_data[city_name]) / len(weather_data[city_name])
        return avg_temp
    else:
        print(f"{city_name} is not in the records.")
        return None

# Sort cities by average temperature (from hottest to coolest)
def sort_cities_by_avg_temp():
    avg_temps = {city: calculate_avg_temperature(city) for city in weather_data}
    sorted_cities = sorted(avg_temps.items(), key=lambda x: x[1], reverse=True)
    print("\nCities sorted by hottest average temperature:")
    for city, avg_temp in sorted_cities:
        print(f"{city}: {avg_temp:.2f}°")
# Add new temperatures for cities
add_temperature("Chennai", 26)
add_temperature("Delhi", 33)
add_temperature("Mumbai", 23)

# Calculate and print average temperatures for each city
print("\nAverage temperatures:")
for city in weather_data:
    avg_temp = calculate_avg_temperature(city)
    print(f"{city}: {avg_temp:.2f}°")

# Sort cities by average temperature (hottest first)
sort_cities_by_avg_temp()
