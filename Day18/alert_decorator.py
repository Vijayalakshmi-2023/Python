import functools

def alert_if_exceeds(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"🚨 ALERT: {func.__name__} returned {result} which exceeds threshold {threshold}")
            else:
                print(f"✅ OK: {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator
import random

@alert_if_exceeds(threshold=75)
def read_temperature():
    return random.randint(60, 90)  # Simulated sensor range
for _ in range(5):
    read_temperature()
