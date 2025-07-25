import functools

def validate_types(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for i, (arg, expected) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {i+1} to '{func.__name__}' must be {expected.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@validate_types(int, int)
def add(a, b):
    return a + b

@validate_types(str, str)
def concat(s1, s2):
    return s1 + s2
print(add(5, 10))           # ✅ Works
print(concat("Hello, ", "World!"))  # ✅ Works

print(add("5", 10))         # ❌ Raises TypeError
print(concat("Hi", 7))      # ❌ Raises TypeError
