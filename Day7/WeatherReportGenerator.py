# Input details
city = input("Enter city name: ").strip()
temperature = input("Enter temperature in °C: ").strip()
humidity = input("Enter humidity percentage: ").strip()

# Using f-string
report_fstring = f"Weather in {city}: {temperature}°C, {humidity}% humidity"

# Using + concatenation
report_plus = "Weather in " + city + ": " + temperature + "°C, " + humidity + "% humidity"

# Using .format()
report_format = "Weather in {}: {}°C, {}% humidity".format(city, temperature, humidity)

# Print all 3 versions
print("\nWeather Report:")
print("Using f-string:", report_fstring)
print("Using + concatenation:", report_plus)
print("Using .format():", report_format)
