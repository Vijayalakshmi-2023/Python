import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"[{func.__name__}] Call #{wrapper.call_count}")
        return func(*args, **kwargs)

    wrapper.call_count = 0  # Initialize call count
    wrapper.reset = lambda: setattr(wrapper, 'call_count', 0)  # Add reset attribute
    return wrapper
@count_calls
def greet(name):
    print(f"Hello, {name}!")

@count_calls
def square(n):
    return n * n
greet("Anu")
greet("Banu")
square(5)
square(10)

print(f"greet() was called {greet.call_count} times.")
print(f"square() was called {square.call_count} times.")

# Reset example
greet.reset()
print("greet count reset.")
greet("Cavin")
print(f"greet() was called {greet.call_count} times.")
