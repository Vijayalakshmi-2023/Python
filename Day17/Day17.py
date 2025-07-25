## Basics of Generator Functions 
#Task 1:
def gen_numbers():
    for i in range(1, 11):
        yield i

#Task 2:
def gen_even(n):
    for i in range(2, n+1, 2):
        yield i

#Task 3:
def gen_squares(n):
    for i in range(1, n+1):
        yield i * i

#Task 4:
def gen_chars(s):
    for char in s:
        yield char

#Task 5:
def gen_vowels(s):
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            yield char

#Task 6:
def gen_alphabet():
    for c in 'abcde':
        yield c

g = gen_alphabet()
print(next(g))  # a
print(next(g))  # b
print(next(g))  # c
print(next(g))  # d
print(next(g))  # e

#Task 7:
def simple_gen():
    yield 1
    yield 2

g = simple_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # Raises StopIteration

#Task 8:
def gen_primes():
    for num in range(2, 101):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

#Task 9:
import sys

def list_func():
    return [i for i in range(100000)]

def gen_func():
    for i in range(100000):
        yield i

# Memory comparison
print("List size:", sys.getsizeof(list_func()))       # Higher memory usage
print("Generator size:", sys.getsizeof(gen_func()))   # Much smaller

#Task 10:
def gen_positive(nums):
    for num in nums:
        if num > 0:
            yield num



##Intermediate Generator Logic  
#Task 11:
def word_generator(paragraph):
    for word in paragraph.split():
        yield word


#Task 12:
def cumulative_sum_gen(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

#Task 13:
def custom_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

#Task 14:
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

#Task 15:
def factorial_gen(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

#Task 16:
def powers_of_two(limit):
    power = 1
    while power <= limit:
        yield power
        power *= 2

#Task 17:
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

#Task 18:
def even_filter(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

#Task 19:
def number_gen(n):
    for i in range(1, n + 1):
        yield i

def square_gen(gen):
    for num in gen:
        yield num ** 2

# Example use:
g1 = number_gen(5)
g2 = square_gen(g1)

#Task 20:
def reverse_string_gen(s):
    for char in reversed(s):
        yield char



##Generator Expressions  
#Task 21:
squares = (x**2 for x in range(1, 11))

#Task 22:
numbers = [1, 4, 7, 10, 13, 16]
odds = (x for x in numbers if x % 2 != 0)

#Task 23:
squares = (x**2 for x in range(1, 6))
squares_list = list(squares)
print(squares_list)  # Output: [1, 4, 9, 16, 25]

#Task 24:
sentence = "Generators are useful for handling large datasets efficiently"
long_words = (word for word in sentence.split() if len(word) > 5)

#Task 25:
text = "PyThOn GeNEraTor"
upper_letters = (ch for ch in text if ch.isupper())

#Task 26:
import sys

gen_expr = (x*x for x in range(1000000))
list_comp = [x*x for x in range(1000000)]

print("Generator size:", sys.getsizeof(gen_expr))    # Very small
print("List comprehension size:", sys.getsizeof(list_comp))  # Much larger

#Task 27:
total = sum(x for x in range(1, 101))  # Sum from 1 to 100

#Task 28:
mixed = [10, 3.5, 'hello', 4.0, True, 7.8]
floats = (x for x in mixed if isinstance(x, float))

#Task 29:
nums = [10, 22, 14, 9, 5]
has_div_3 = any(x % 3 == 0 for x in nums)


#Task 30:
values = [12, 99, 27, 34]
highest = max(x for x in values)



## Advanced Generator Techniques 
#Task 31:
def infinite_multiples_of_5():
    i = 1
    while True:
        yield i * 5
        i += 1

#Task 32:
def chunk_in_threes(iterable):
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == 3:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

#Task 33:
def sorted_names(names):
    for name in sorted(names):
        yield name

#Task 34:
def reversed_lines(file_path):
    with open(file_path, 'r') as file:
        for line in reversed(file.readlines()):
            yield line.strip()

#Task 35:
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

#Task 36:
def logging_generator():
    print("Yielding 1")
    yield 1
    print("Yielding 2")
    yield 2
    print("Yielding 3")
    yield 3

#Task 37:
def double_receiver():
    while True:
        val = yield
        print("Received:", val)
        yield val * 2
gen = double_receiver()
next(gen)             # Prime the generator
print(gen.send(4))    # Output: 8


#Task 38:
def sum_up_to(n):
    total = 0
    for i in range(1, n+1):
        total += i
        yield i
    return total

gen = sum_up_to(5)
try:
    while True:
        print(next(gen))
except StopIteration as e:
    print("Returned value:", e.value)  # Total sum

#Task 39:
def csv_line_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip().split(',')

#Task 40:
def yield_tracker(n):
    count = 0
    for i in range(n):
        count += 1
        print(f"Yield called {count} time(s)")
        yield i


## Real-Life Generator Use Cases 
#Task 41:
def log_reader(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
for log in log_reader("system.log"):
    print(log)

#Task 42:
import time
import random

def sensor_data():
    while True:
        value = round(random.uniform(20.0, 30.0), 2)  # Simulated temperature
        yield value
        time.sleep(1)
for data in sensor_data():
    print(f"Sensor Reading: {data}")

#Task 43:
def mock_api():
    # Simulate a dataset of 100 items
    data = [f"Item {i}" for i in range(1, 101)]
    page_size = 10
    for i in range(0, len(data), page_size):
        yield data[i:i+page_size]
for page in mock_api():
    print("Page:", page)

#Task 44:
import time
import random

def stock_price_monitor(symbol):
    price = 100.0  # Starting price
    while True:
        # Simulate small price fluctuations
        price += random.uniform(-1, 1)
        yield f"{symbol}: ${price:.2f}"
        time.sleep(1)
for update in stock_price_monitor("AAPL"):
    print(update)

#Task 45:
def form_validator(form_data):
    if not form_data.get("username"):
        yield "Username is required"
    if not form_data.get("email") or "@" not in form_data["email"]:
        yield "Invalid email"
    if len(form_data.get("password", "")) < 6:
        yield "Password must be at least 6 characters"
    yield "Form validation complete"
form = {"username": "", "email": "test@", "password": "123"}
for result in form_validator(form):
    print(result)


## Generator Comparison and Integration  
#Task 46:
import time
import sys

# List approach
start_list = time.time()
lst = [i for i in range(10_000_000)]
for x in lst:
    pass
end_list = time.time()

# Generator approach
start_gen = time.time()
gen = (i for i in range(10_000_000))
for x in gen:
    pass
end_gen = time.time()

print("List iteration time:", end_list - start_list)
print("Generator iteration time:", end_gen - start_gen)
print("List memory usage:", sys.getsizeof(lst))        # Large
print("Generator memory usage:", sys.getsizeof(gen))   # Very small

#Task 47:
gen = (x for x in range(1, 11))  # Generator from 1 to 10
squared = map(lambda x: x**2, gen)

for val in squared:
    print(val)
def square(x): return x**2
squared = map(square, gen)

#Task 48:
def number_gen(n):
    for i in range(1, n + 1):
        yield i

def even_filter(gen):
    for num in gen:
        if num % 2 == 0:
            yield num

def square_gen(gen):
    for num in gen:
        yield num ** 2
pipeline = square_gen(even_filter(number_gen(10)))
for result in pipeline:
    print(result)  # Output: 4, 16, 36, 64, 100

#Task 49:
def command_reader():
    commands = ["start", "status", "stop", "exit"]
    for cmd in commands:
        print(f">>> {cmd}")
        yield cmd
for command in command_reader():
    if command == "exit":
        print("Exiting...")
        break
    else:
        print(f"Command received: {command}")

#Task 50:
import re

def valid_email_gen(emails):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    for email in emails:
        if pattern.match(email):
            yield email
import unittest

class TestValidEmailGen(unittest.TestCase):
    def test_valid_emails(self):
        input_emails = [
            "test@example.com",
            "invalid-email",
            "user@domain",
            "admin@site.org",
            "hello@world123.com"
        ]
        expected = [
            "test@example.com",
            "admin@site.org",
            "hello@world123.com"
        ]
        result = list(valid_email_gen(input_emails))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

