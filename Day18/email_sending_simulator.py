import functools
import time
import datetime

def retry(max_retries=2, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt <= max_retries:
                try:
                    attempt += 1
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"[{datetime.datetime.now()}] Attempt {attempt} FAILED: {e}")
                    if attempt > max_retries:
                        print(f"[{datetime.datetime.now()}] All {max_retries + 1} attempts failed.")
                        return None
                    time.sleep(delay)
        return wrapper
    return decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            result = func(*args, **kwargs)
            print(f"[{timestamp}] SUCCESS: {func.__name__} | Args: {args}, Kwargs: {kwargs}")
            return result
        except Exception as e:
            print(f"[{timestamp}] ERROR: {func.__name__} | Args: {args}, Kwargs: {kwargs} | Exception: {e}")
            raise
    return wrapper
import random

@retry(max_retries=2, delay=1)
@log
def send_email(to, subject, body):
    if random.random() < 0.7:  # Simulate failure 70% of the time
        raise ConnectionError("Email server not responding.")
    return f"Email sent to {to} with subject '{subject}'"
print(send_email("test@example.com", "Welcome", "Hello there!"))
