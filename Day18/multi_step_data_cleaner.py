import functools

# 1. Remove null (None) values
def remove_nulls(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item for item in data if item is not None]
        return func(cleaned)
    return wrapper

# 2. Strip whitespace from strings
def strip_whitespace(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.strip() if isinstance(item, str) else item for item in data]
        return func(cleaned)
    return wrapper

# 3. Convert strings to lowercase
def to_lowercase(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.lower() if isinstance(item, str) else item for item in data]
        return func(cleaned)
    return wrapper
@remove_nulls
@strip_whitespace
@to_lowercase
def process_data(data):
    print("Cleaned Data:", data)
raw_data = ["  Anu ", None, " Banu", "   Cavin ", "", None, "Diya  "]
process_data(raw_data)
