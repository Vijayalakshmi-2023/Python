import functools
import time
import datetime

def retry(max_retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    attempts += 1
                    print(f"[{datetime.datetime.now()}] Attempt {attempts} for {func.__name__}")
                    result = func(*args, **kwargs)
                    print(f"[{datetime.datetime.now()}] Success on attempt {attempts}")
                    print("-" * 50)
                    return result
                except Exception as e:
                    print(f"[{datetime.datetime.now()}] Error on attempt {attempts}: {e}")
                    if attempts < max_retries:
                        time.sleep(delay)
            print(f"[{datetime.datetime.now()}] All {max_retries} attempts failed for {func.__name__}")
            print("-" * 50)
            return None
        return wrapper
    return decorator
import random

@retry(max_retries=3, delay=1)
def unstable_api_call():
    if random.random() < 0.7:  # 70% chance to fail
        raise ConnectionError("Network issue occurred.")
    return "API call successful!"
print(unstable_api_call())
