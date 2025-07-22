# data_ops.py

def add_weather_data(log, date, temp, humidity, condition):
    log[date] = (temp, humidity, condition)
    return f"✅ Weather logged for {date}: {temp}°C, {humidity}%, {condition}"

def view_weather_data(log, date):
    if date in log:
        temp, humidity, condition = log[date]
        return f"📅 {date} → Temp: {temp}°C, Humidity: {humidity}%, Condition: {condition}"
    else:
        return "❌ No data for that date."
