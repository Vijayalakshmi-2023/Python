import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {func.__name__}{args}")
            return cache[args]
        
        print(f"Cache miss for {func.__name__}{args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper
@memoize
def slow_square(n):
    print(f"Computing square of {n}...")
    return n * n

@memoize
def add(a, b):
    return a + b
print(slow_square(4))  # Computes and caches
print(slow_square(4))  # Returns cached

print(add(2, 3))        # Computes and caches
print(add(2, 3))        # Returns cached
print(add(3, 2))        # Different args, not cached
