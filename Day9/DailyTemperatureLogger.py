# Sample temperature data for a week, each entry is a tuple (date, (morning_temp, evening_temp))
temperature_data = [
    ("2025-07-01", (25, 30)),
    ("2025-07-02", (26, 32)),
    ("2025-07-03", (28, 31)),
    ("2025-07-04", (27, 33)),
    ("2025-07-05", (29, 35)),
    ("2025-07-06", (30, 34)),
    ("2025-07-07", (31, 36)),
    ("2025-07-08", (32, 38)),
    ("2025-07-09", (33, 39)),
    ("2025-07-10", (34, 40))
]

# 1. Get data for the last 7 days using slicing
def last_seven_days_data():
    print("Data for the last 7 days:")
    last_7_days = temperature_data[-7:]  # Slicing the last 7 days
    for date, (morning_temp, evening_temp) in last_7_days:
        print(f"Date: {date}, Morning Temp: {morning_temp}°C, Evening Temp: {evening_temp}°C")
    print("-" * 30)

# 2. Find the highest evening temperature using max()
def highest_evening_temp():
    highest_temp_data = max(temperature_data, key=lambda data: data[1][1])  # Max by evening temperature
    date, (morning_temp, evening_temp) = highest_temp_data  # Unpacking
    print(f"The highest evening temperature was on {date} with {evening_temp}°C.")

# 3. Generate a report with temperature analysis using tuple unpacking
def temperature_analysis_report():
    print("Temperature Analysis Report:")
    total_morning_temp = 0
    total_evening_temp = 0
    for date, (morning_temp, evening_temp) in temperature_data:
        total_morning_temp += morning_temp
        total_evening_temp += evening_temp
    
    avg_morning_temp = total_morning_temp / len(temperature_data)
    avg_evening_temp = total_evening_temp / len(temperature_data)
    
    print(f"Average Morning Temperature: {avg_morning_temp:.2f}°C")
    print(f"Average Evening Temperature: {avg_evening_temp:.2f}°C")
    print("-" * 30)

# Testing the functions
last_seven_days_data()  # Show data for the last 7 days
highest_evening_temp()  # Find the highest evening temperature
temperature_analysis_report()  # Generate temperature analysis report
