import random

def temperature_sensor():
    override = None
    while True:
        # Use override if sent, else generate random value
        temp = yield override if override is not None else random.uniform(60.0, 105.0)
        override = temp  # Injected override replaces next reading
def get_reading(sensor_gen):
    return round(next(sensor_gen), 2)

# Set sentinel to break the stream at temperature > 100
def lazy_temp_stream(sensor_gen):
    return iter(lambda: get_reading(sensor_gen), None)
sensor = temperature_sensor()
next(sensor)  # Prime the generator

for i, temp in enumerate(lazy_temp_stream(sensor), start=1):
    print(f"Reading {i}: {temp}°F")

    # Inject manual override at 5th reading
    if i == 5:
        sensor.send(72.5)  # Override with a custom value
        print("Manual override: 72.5°F")

    # Stop if reading is above 100
    if temp > 100:
        print("CRITICAL: Temperature exceeded 100°F. Shutting down stream.")
        break
