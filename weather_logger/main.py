# main.py

from data_ops import add_weather_data, view_weather_data
from analysis import monthly_summary, unique_conditions

weather_log = {}

# Sample entries
print(add_weather_data(weather_log, "2025-07-21", 32, 65, "Sunny"))
print(add_weather_data(weather_log, "2025-07-22", 30, 70, "Cloudy"))
print(add_weather_data(weather_log, "2025-07-23", 31, 60, "Rainy"))

# View single day
print("\n🔍 View Data:")
print(view_weather_data(weather_log, "2025-07-22"))

# Monthly summary
print("\n📈 Monthly Summary:")
print(monthly_summary(weather_log, "2025-07"))

# Unique weather conditions
print("\n🌈 Unique Weather Conditions:")
print(", ".join(unique_conditions(weather_log)))
