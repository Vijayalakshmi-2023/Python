import functools

def validate_numeric_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argument {i+1} of '{func.__name__}' must be int or float, got {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper
def log_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] Args: {args}, Result: {result}")
        return result
    return wrapper
import time
import datetime

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Execution Time for {func.__name__}: {duration:.6f}s")
        return result
    return wrapper
@timeit
@log_output
@validate_numeric_input
def add(a, b):
    return a + b

@timeit
@log_output
@validate_numeric_input
def multiply(a, b):
    return a * b

@timeit
@log_output
@validate_numeric_input
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
add(5, 3)
multiply(4, 2.5)
try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    add(5, "two")
except TypeError as e:
    print(f"Error: {e}")
