## Basic Decorator Tasks 
#Task 1:
def start_message(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper

#Task 2:
def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

#Task 3:
def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper

#Task 4:
def square_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

#Task 5:
def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

#Task 6:
def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

#Task 7:
def log_before_after(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

#Task 8:
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in {func.__name__}: {e}")
    return wrapper

#Task 9:
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

#Task 10:
from datetime import datetime

def log_datetime(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@start_message
@print_function_name
@count_calls
def greet(name):
    return f"Hello, {name}"

greet("Anu")
greet("Banu")


## Decorators with *args and **kwargs  
#Task 11:
def log_all_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments for {func.__name__} → args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

#Task 12:
def sum_args(func):
    def wrapper(*args, **kwargs):
        total = sum(arg for arg in args if isinstance(arg, (int, float)))
        print(f"Sum of positional numeric arguments: {total}")
        return func(*args, **kwargs)
    return wrapper

#Task 13:
def validate_types(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, typ) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, typ):
                    raise TypeError(f"Argument {i+1} must be {typ.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Task 14:
def non_empty_string(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and not arg.strip():
                raise ValueError("String arguments must not be empty.")
        return func(*args, **kwargs)
    return wrapper

#Task 15:
def require_keyword_arg(func):
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument is required.")
        return func(*args, **kwargs)
    return wrapper

#Task 16:
def only_ints(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("All positional arguments must be integers.")
        return func(*args, **kwargs)
    return wrapper

#Task 17:
def reverse_list_arg(func):
    def wrapper(arg, *args, **kwargs):
        if isinstance(arg, list):
            arg = arg[::-1]
        return func(arg, *args, **kwargs)
    return wrapper

#Task 18:
def lowercase_strings(func):
    def wrapper(*args, **kwargs):
        args = tuple(arg.lower() if isinstance(arg, str) else arg for arg in args)
        kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper

#Task 19:
def round_floats(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result
    return wrapper

#Task 20:
def block_if_requested(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('block', False):
            print("⚠️ Function execution blocked due to 'block=True'")
            return None
        return func(*args, **kwargs)
    return wrapper
@log_all_args
@sum_args
@only_ints
def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3, 5))

@block_if_requested
def send_data(data, **kwargs):
    print("Data sent:", data)

send_data("TOP_SECRET", block=True)


## Decorators with Parameters (Decorator Factory) 
#Task 21:
def repeat_output(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return [result for _ in range(n)]
        return wrapper
    return decorator

#Task 22:
import datetime

def log_to_file(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(f"{datetime.datetime.now()} - {func.__name__} called with {args}, {kwargs} → {result}\n")
            return result
        return wrapper
    return decorator

#Task 23:
def limit_calls(max_calls):
    def decorator(func):
        count = {"calls": 0}
        def wrapper(*args, **kwargs):
            if count["calls"] >= max_calls:
                print("⚠️ Function call limit reached.")
                return None
            count["calls"] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Task 24:
def role_required(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(f"User does not have required role: {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

#Task 25:
def min_args_length(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) < n:
                raise ValueError(f"Function requires at least {n} positional arguments.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Task 26:
def log_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} → Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Task 27:
import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"⏳ Delaying execution by {seconds} seconds...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Task 28:
def add_banner(header, footer):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

#Task 29:
import time

def warn_if_slow(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            if duration > threshold:
                print(f"⚠️ WARNING: {func.__name__} took {duration:.2f}s (threshold: {threshold}s)")
            return result
        return wrapper
    return decorator

#Task 30:
def apply_to_result(transform_fn):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform_fn(result)
        return wrapper
    return decorator
@limit_calls(2)
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")
greet("Eve")  # blocked

@delay(2)
@add_banner("=== START ===", "=== END ===")
def say_hi():
    print("Hi there!")

say_hi()


## Multiple Decorators and Chaining
#Task 31:
from functools import wraps

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

def square_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@double_result
@square_result
def get_number():
    return 3  # (3^2)=9 → (9*2)=18

#Task 32:
def authenticate(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError("User not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

def authorize(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Unauthorized access")
        return func(user, *args, **kwargs)
    return wrapper

@authenticate
@authorize
def delete_user(user):
    return "User deleted"

#Task 33:
def log_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Input: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_input
@log_output
def multiply(x, y):
    return x * y

#Task 34:
def reverse_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)[::-1]
    return wrapper

def uppercase_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@reverse_string
@uppercase_string
def greet():
    return "hello"  # → "HELLO" → "OLLEH"

#Task 35:
def html_p(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

def html_div(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper

@html_p
@html_div
def get_html_text():
    return "Welcome!"

#Task 36:
import time

def cli_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

def cli_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] Took {time.time() - start:.4f}s")
        return result
    return wrapper

def cli_formatter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"[RESULT] {func(*args, **kwargs)}"
    return wrapper

@cli_logger
@cli_timer
@cli_formatter
def run_cli():
    time.sleep(0.5)
    return "CLI executed"

#Task 37:
def log_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def check_even(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            print("Even number ✅")
        else:
            print("Odd number ❌")
        return result
    return wrapper

@check_even
@log_result
def compute():
    return 6

#Task 38:
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x < 0:
            raise ValueError("Only positive numbers allowed")
        return func(x)
    return wrapper

def double_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

@double_output
@validate_positive
def increment(x):
    return x + 1

#Task 39:
def stage_one(func):
    @wraps(func)
    def wrapper(data):
        print("Stage 1: Cleaning")
        return func(data.strip())
    return wrapper

def stage_two(func):
    @wraps(func)
    def wrapper(data):
        print("Stage 2: Lowercasing")
        return func(data.lower())
    return wrapper

def stage_three(func):
    @wraps(func)
    def wrapper(data):
        print("Stage 3: Analyzing")
        return func(data)
    return wrapper

@stage_three
@stage_two
@stage_one
def process_pipeline(data):
    return f"Processed: {data}"

#Task 40:
def preserve(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve
def sample_function():
    """This function does nothing."""
    pass

print(sample_function.__name__)   # 'sample_function'
print(sample_function.__doc__)    # 'This function does nothing.'


## Class-based Decorators and Built-in Types  
#Task 41:
from functools import wraps

class LogDecorator:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[LOG] Starting {self.func.__name__}()")
        result = self.func(*args, **kwargs)
        print(f"[LOG] Finished {self.func.__name__}()")
        return result

@LogDecorator
def greet(name):
    print(f"Hello, {name}!")

#Task 42:
class Memoize:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print("[CACHE HIT]")
            return self.cache[args]
        print("[CACHE MISS]")
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

#Task 43:
class InstanceTracker:
    def __init__(self, cls):
        self.cls = cls
        self.instance_count = 0
        wraps(cls)(self)

    def __call__(self, *args, **kwargs):
        self.instance_count += 1
        print(f"[INFO] {self.cls.__name__} instance #{self.instance_count} created")
        return self.cls(*args, **kwargs)

@InstanceTracker
class Person:
    def __init__(self, name):
        self.name = name

#Task 44:
def log_method_call(func):
    @wraps(func)
    def wrapper(cls, *args, **kwargs):
        print(f"[CLASS LOG] Calling {cls.__name__}.{func.__name__}")
        return func(cls, *args, **kwargs)
    return wrapper

class MyClass:
    @classmethod
    @log_method_call
    def say_hello(cls):
        print(f"Hello from {cls.__name__}")

#Task 45:
def log_property_access(prop_func):
    @property
    @wraps(prop_func)
    def wrapper(self):
        print(f"[ACCESS LOG] Accessing {prop_func.__name__}")
        return prop_func(self)
    return wrapper

class Product:
    def __init__(self, price):
        self._price = price

    @log_property_access
    def price(self):
        return self._price


## Advanced Practical Decorators 
#Task 46:
import time
from functools import wraps
from collections import deque

def rate_limit(max_calls=5, per_seconds=60):
    calls = deque()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while calls and current_time - calls[0] > per_seconds:
                calls.popleft()

            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded. Try again later.")
            
            calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit()
def fetch_data():
    print("API data fetched.")

#Task 47:
def retry(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry {attempts+1}] Failed: {e}")
                    attempts += 1
            raise Exception("Max retries exceeded.")
        return wrapper
    return decorator

@retry()
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success"

#Task 48:
call_log = []

def track_call_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        call_log.append((func.__name__, timestamp))
        return func(*args, **kwargs)
    return wrapper

@track_call_time
def process():
    print("Function processed.")

#Task 49:
def secure_token(required_token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get('token')
            if token != required_token:
                raise PermissionError("Invalid API token.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@secure_token("secret123")
def get_sensitive_data(*, token=None):
    return "Sensitive Data"

#Task 50:
def encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def encryption_decorator(key):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, str):
                raise TypeError("Encryption supports only string return values.")
            encrypted = encrypt(result, key)
            decrypted = encrypt(encrypted, key)
            print(f"[Encrypted]: {encrypted.encode('utf-8')}")
            print(f"[Decrypted]: {decrypted}")
            return decrypted
        return wrapper
    return decorator

@encryption_decorator("mykey")
def secret_message():
    return "This is top secret!"
