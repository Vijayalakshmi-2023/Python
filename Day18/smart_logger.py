import functools
import datetime

def smart_logger(log_level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                log_message = (
                    f"[{timestamp}] [{log_level}] Function: {func.__name__} | "
                    f"Args: {args}, Kwargs: {kwargs} | Result: {result}\n"
                )
            except Exception as e:
                log_message = (
                    f"[{timestamp}] [ERROR] Function: {func.__name__} | "
                    f"Args: {args}, Kwargs: {kwargs} | Exception: {e}\n"
                )
                result = None

            # Write to file
            with open("log.txt", "a") as file:
                file.write(log_message)

            return result
        return wrapper
    return decorator
@smart_logger(log_level="INFO")
def multiply(a, b):
    return a * b

@smart_logger(log_level="DEBUG")
def greet(name):
    return f"Hello, {name}!"

@smart_logger(log_level="WARNING")
def divide(a, b):
    return a / b  # might raise ZeroDivisionError
multiply(5, 6)
greet("Vijayalakshmi")
divide(10, 0)
