import functools
import time
import datetime
from collections import deque

def throttle(max_calls_per_minute):
    def decorator(func):
        call_times = deque()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove timestamps older than 60 seconds
            while call_times and now - call_times[0] > 60:
                call_times.popleft()

            if len(call_times) >= max_calls_per_minute:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] BLOCKED: Too many calls to '{func.__name__}'")
                raise RuntimeError(f"Throttle limit exceeded: max {max_calls_per_minute} calls per minute.")

            call_times.append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator
@throttle(3)  # Allow max 3 calls per minute
def fetch_data():
    print(f"Fetched data at {datetime.datetime.now().strftime('%H:%M:%S')}")
for i in range(5):
    try:
        fetch_data()
    except RuntimeError as e:
        print(e)
    time.sleep(1)  # Try changing to 20 to simulate spaced-out access

