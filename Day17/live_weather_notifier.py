import random
import time
def weather_data_stream():
    current_temp = random.randint(20, 30)
    while True:
        time.sleep(1)  # Simulate delay (1 second)
        fluctuation = random.randint(-3, 6)
        new_temp = current_temp + fluctuation
        yield new_temp
        current_temp = new_temp
def significant_change_filter(stream, threshold=5):
    prev_temp = next(stream)
    for temp in stream:
        if abs(temp - prev_temp) >= threshold:
            yield (prev_temp, temp)
        prev_temp = temp
try:
    print("🌡️ Live Weather Notifier (±5°C changes only)")
    raw_stream = weather_data_stream()
    filtered_stream = significant_change_filter(raw_stream)

    for prev, curr in filtered_stream:
        print(f"⚠️ Temp change from {prev}°C → {curr}°C")
except KeyboardInterrupt:
    print("\n🛑 Weather monitoring stopped by user.")
