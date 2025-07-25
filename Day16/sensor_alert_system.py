import random

def read_sensor():
    value = random.randint(50, 100)
    print(f"Sensor reading: {value}")
    return value

# Create an iterator that stops when 99 is returned
sensor_iterator = iter(read_sensor, 99)

for reading in sensor_iterator:
    pass  # Values are printed inside read_sensor()

print("🚨 ALERT: Critical sensor value (99) reached!")
