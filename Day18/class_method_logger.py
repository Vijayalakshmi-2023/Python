import functools

def log_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        # Only wrap callable instance methods, skip dunder methods
        if callable(attr_value) and not attr_name.startswith("__"):
            @functools.wraps(attr_value)
            def wrapper(self, *args, __func=attr_value, **kwargs):
                print(f"[LOG] {cls.__name__}.{__func.__name__} called with args={args}, kwargs={kwargs}")
                return __func(self, *args, **kwargs)
            setattr(cls, attr_name, wrapper)
    return cls
@log_methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, x, y):
        return x * y

    def power(self, base, exponent=2):
        return base ** exponent
calc = Calculator()
print("Result:", calc.add(5, 3))
print("Result:", calc.multiply(4, 6))
print("Result:", calc.power(2))
