##Basic Iterator and Iterable Understanding
#Task 1:  
lst = [10, 20, 30]
it = iter(lst)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

#Task 2: 
# Using for loop
tpl = (1, 2, 3)
for item in tpl:
    print(item)

# Using while with next()
it = iter(tpl)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

#Task 3: 
def is_iterable(obj):
    return '__iter__' in dir(obj)

print(is_iterable([1, 2, 3]))   # True
print(is_iterable(42))         # False

#Task 4:
non_iterator = 100
try:
    print(next(non_iterator))
except TypeError as e:
    print(f"Error: {e}")  # next() can't be used on int

#Task 5: 
my_set = {10, 20, 30, 40}
it = iter(my_set)
for _ in range(3):
    print(next(it))

#Task 6: 
s = "hello"
it = iter(s)
print(next(it))  # h
print(next(it))  # e
print(next(it))  # l

#Task 7: 
d = {'a': 1, 'b': 2, 'c': 3}
it = iter(d)
print(next(it))  # a
print(next(it))  # b

#Task 8: 
r = range(5)
it = iter(r)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

#Task 9: 
def consume_iterable(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

consume_iterable(['a', 'b', 'c'])

#Task 10:
# it = iter([1, 2])
print(next(it))  # 1
print(next(it))  # 2
try:
    print(next(it))  # raises StopIteration
except StopIteration:
    print("No more items left.")
 



##Custom Iterator Classes  
#Task 11:
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Example
for num in Countdown(5):
    print(num)
  
#Task 12: 
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current += 2
        return val

# Example
for num in EvenNumbers(10):
    print(num)

#Task 13: 
class CharIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        ch = self.text[self.index]
        self.index += 1
        return ch

# Example
for ch in CharIterator("Python"):
    print(ch)

#Task 14:
class FibonacciIterator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_val:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

# Example
for num in FibonacciIterator(21):
    print(num)

#Task 15: 
class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        val = self.lst[self.index]
        self.index -= 1
        return val

# Example
for item in ReverseListIterator([1, 2, 3, 4]):
    print(item)

#Task 16: 
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current ** 2
        self.current += 1
        return val

# Example
for square in SquareIterator(1, 5):
    print(square)

#Task 17: 
class LetterPositionIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        result = (self.text[self.index], self.index)
        self.index += 1
        return result

# Example
for ch, pos in LetterPositionIterator("abc"):
    print(f"{ch} at {pos}")

#Task 18: 
class CountdownWithStop:
    def __init__(self, start, stop_at):
        self.current = start
        self.stop_at = stop_at

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_at:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Example
for num in CountdownWithStop(10, 5):
    print(num)

#Task 19: 
class VowelIterator:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.vowels = 'aeiouAEIOU'

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.sentence):
            ch = self.sentence[self.index]
            self.index += 1
            if ch in self.vowels:
                return ch
        raise StopIteration

# Example
for vowel in VowelIterator("Hello World! How are you?"):
    print(vowel)

#Task 20: 
class DigitIterator:
    def __init__(self, mixed_string):
        self.mixed_string = mixed_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.mixed_string):
            ch = self.mixed_string[self.index]
            self.index += 1
            if ch.isdigit():
                return ch
        raise StopIteration

# Example
for digit in DigitIterator("abc123def45gh6"):
    print(digit)



##Advanced Use of iter()  
#Task 21:  
for line in iter(input, "exit"):
    print(f"You said: {line}")

#Task 22:
def read_file_until_stop(file_path, stop_line="STOP\n"):
    with open(file_path, 'r') as f:
        for line in iter(f.readline, stop_line):
            print(line.strip())

# Usage (ensure the file exists):
# read_file_until_stop("sample.txt")
 
#Task 23: 
import random

def get_number():
    return random.randint(1, 100)

for num in iter(get_number, 91):  # It stops only if it hits 91 exactly, so:
    print(num)
    if num > 90:
        print("Stopping, number > 90")
        break

#Task 24:
for num in iter(lambda: int(input("Enter number: ")), 0):
    print(f"You entered: {num}")

#Task 25: 
class AlphaOnlyIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            ch = self.text[self.index]
            self.index += 1
            if ch.isalpha():
                return ch
        raise StopIteration

# Example
for char in AlphaOnlyIterator("He110 W0rld!"):
    print(char)

#Task 26: 
import itertools

infinite_numbers = iter(lambda: random.randint(1, 100), None)
# Warning: This is infinite — break manually
for i, val in enumerate(infinite_numbers):
    print(val)
    if i == 9:  # Stop after 10 numbers
        break

#Task 27: 
for expr in iter(input, "done"):
    try:
        print(f"Result: {eval(expr)}")
    except Exception as e:
        print(f"Error: {e}")

#Task 28: 
import math

def input_numbers():
    return float(input("Enter number: "))

for num in iter(input_numbers, 0.0):  # Enter 0 to stop
    try:
        print(f"Sqrt: {math.sqrt(num)}")
    except ValueError:
        print("Invalid input for sqrt.")

#Task 29: 
def manual_iterator(iterable):
    it = iter(iterable)
    index = 0
    while True:
        try:
            value = next(it)
            print(f"Index {index}: {value}")
            index += 1
        except StopIteration:
            break

manual_iterator(['a', 'b', 'c'])

#Task 30: 
count = 0
for _ in iter(input, "stop"):
    count += 1
print(f"You entered {count} items before stopping.")


## Iterator with Files 
#Task 31:  
with open("sample.txt", "r") as file:
    file_iterator = iter(file)
    print(next(file_iterator))  # Read first line
    print(next(file_iterator))  # Read second line

#Task 32: 
with open("sample.txt", "r") as file:
    file_iterator = iter(file)
    while True:
        try:
            line = next(file_iterator)
            print(line.strip())
        except StopIteration:
            print("Reached end of file.")
            break

#Task 33: 
class NonEmptyLineIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if line == "":  # EOF
                self.file.close()
                raise StopIteration
            if line.strip():  # Non-empty
                return line.strip()

# Usage
for line in NonEmptyLineIterator("sample.txt"):
    print(line)

#Task 34:
class FirstWordIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            words = line.strip().split()
            if words:
                return words[0]

# Usage
for word in FirstWordIterator("sample.txt"):
    print(word)

#Task 35: 
class LongLineIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if line == "":
                self.file.close()
                raise StopIteration
            if len(line.strip().split()) > 3:
                return line.strip()

# Usage
for line in LongLineIterator("sample.txt"):
    print(line)


## Loop Integration and Comparison 
#Task 36: 
import time

data = list(range(10_000_000))  # 10 million items

# For loop
start = time.time()
for item in data:
    pass
for_duration = time.time() - start

# While with next()
start = time.time()
it = iter(data)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
while_duration = time.time() - start

print(f"For loop: {for_duration:.5f} sec")
print(f"While + next(): {while_duration:.5f} sec")

#Task 37: 
class SkipAlternateIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self.iterable)  # Get current item
        try:
            next(self.iterable)    # Skip next item
        except StopIteration:
            pass
        return val

# Example
for item in SkipAlternateIterator([1, 2, 3, 4, 5, 6]):
    print(item)  # Outputs: 1, 3, 5

#Task 38: 
class ZipLikeIterator:
    def __init__(self, iterable1, iterable2):
        self.it1 = iter(iterable1)
        self.it2 = iter(iterable2)

    def __iter__(self):
        return self

    def __next__(self):
        return (next(self.it1), next(self.it2))

# Example
for a, b in ZipLikeIterator([1, 2, 3], ['a', 'b', 'c']):
    print(a, b)

#Task 39: 
class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._peek = None
        self._has_peeked = False

    def __iter__(self):
        return self

    def peek(self):
        if not self._has_peeked:
            self._peek = next(self.iterator)
            self._has_peeked = True
        return self._peek

    def __next__(self):
        if self._has_peeked:
            self._has_peeked = False
            return self._peek
        return next(self.iterator)

# Example
p = Peekable([10, 20, 30])
print(p.peek())  # 10
print(next(p))   # 10
print(next(p))   # 20

#Task 40: 
class CircularIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        val = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return val

# Example: stop manually after 8 iterations
circle = CircularIterator([1, 2, 3])
for _ in range(8):
    print(next(circle))  # 1 2 3 1 2 3 1 2



## Exception Handling and Edge Cases  
#Task 41:  
list1 = [1, 2, 3]
list2 = [4, 5, 6]

it1 = iter(list1)
it2 = iter(list2)

while True:
    try:
        print(next(it1))
    except StopIteration:
        print("Switched to second list.")
        break

for val in it2:
    print(val)

#Task 42: 
class LimitReachedError(Exception):
    pass

class FiveItemIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 5:
            raise LimitReachedError("Limit of 5 items reached!")
        self.count += 1
        return next(self.it)

# Example
try:
    for item in FiveItemIterator([10, 20, 30, 40, 50, 60, 70]):
        print(item)
except LimitReachedError as e:
    print(e)

#Task 43: 
class CustomStopIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration("No more items left in the iterator!")
        val = self.data[self.index]
        self.index += 1
        return val

# Example
it = CustomStopIterator([1, 2])
try:
    while True:
        print(next(it))
except StopIteration as e:
    print(f"Stopped: {e}")

#Task 44: 
class SafeIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            return None  # Return None instead of raising

# Example
it = SafeIterator([1, 2, 3])
while True:
    item = next(it)
    if item is None:
        break
    print(item)

#Task 45:
class WarningIterator:
    def __init__(self, iterable):
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            print("⚠️  Warning: Iterator has no more items!")
            raise

# Example
try:
    for x in WarningIterator([10, 20]):
        print(x)
    next(WarningIterator([]))  # force warning
except StopIteration:
    pass


## Real-Life Use Case Based Iterators  
#Task 46: 
class PaginationIterator:
    def __init__(self, articles, page_size):
        self.articles = articles
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.articles):
            raise StopIteration
        page = self.articles[self.index:self.index + self.page_size]
        self.index += self.page_size
        return page

# Example
articles = [f"Post {i}" for i in range(1, 11)]
for page in PaginationIterator(articles, 3):
    print(page)

#Task 47: 
class TransactionIterator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.transactions):
            raise StopIteration
        batch = self.transactions[self.index:self.index + 5]
        self.index += 5
        return batch

# Example
transactions = [f"Txn-{i}" for i in range(1, 17)]
for group in TransactionIterator(transactions):
    print(group)

#Task 48: 
class SensorDataIterator:
    def __init__(self, data, threshold):
        self.data = data
        self.index = 0
        self.threshold = threshold

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        if value > self.threshold:
            raise StopIteration
        self.index += 1
        return value

# Example
sensor_data = [25, 28, 29, 30, 35, 42, 100]  # Stop at 42
for reading in SensorDataIterator(sensor_data, threshold=40):
    print(reading)

#Task 49:
import re

class EmailValidatorIterator:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0
        self.pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.emails):
            email = self.emails[self.index]
            self.index += 1
            if self.pattern.match(email):
                return email
        raise StopIteration

# Example
emails = ["user@example.com", "invalid@", "admin@mail.com", "wrong@.com"]
for valid_email in EmailValidatorIterator(emails):
    print(valid_email)
 
#Task 50: 
class ProductStockIterator:
    def __init__(self, products, threshold):
        self.products = products  # list of dicts
        self.threshold = threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            if product["stock"] < self.threshold:
                return product
        raise StopIteration

# Example
products = [
    {"name": "Apples", "stock": 50},
    {"name": "Oranges", "stock": 10},
    {"name": "Bananas", "stock": 3}
]
for p in ProductStockIterator(products, threshold=20):
    print(p)




