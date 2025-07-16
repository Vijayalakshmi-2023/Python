##Dictionary Basics
#Task 1. Create a dictionary with five employee names and their ID numbers.
employees = {
    "Anu": 101,
    "Banu": 102,
    "Charu": 103,
    "Diya": 104,
    "Elan": 105
}
print("Employees Dictionary:", employees)


#Task 2. Access and print the phone number from a contact dictionary.
# Defining a contact dictionary
contact = {
    "name": "Joseph",
    "phone": "123-456-7890",
    "email": "joseph@example.com"
}
print("Phone Number:", contact["phone"])


#Task 3. Use the get() method to retrieve a value that may not exist in the dictionary.
# Contact dictionary without an address key
contact = {
    "name": "Joseph",
    "phone": "123-456-7890",
    "email": "joseph@example.com"
}
# Attempting to retrieve the 'address' key using get()
address = contact.get("address", "Address not found")
# Print the result
print("Address:", address)


#Task 4. Add a new key-value pair to a student marks dictionary.
# Existing student marks dictionary
marks = {
    "Anu": 88,
    "Banu": 92
}
# Adding a new student and their marks
marks["Cavin"] = 85
# Print the updated dictionary
print("Updated Marks Dictionary:", marks)


#Task 5. Update an existing student's score in the marks dictionary.
# Existing student marks dictionary
marks = {
    "Anu": 91,
    "Banu": 92,
    "Cavin": 85
}
# Updating Anna's score
marks["Anu"] = 91
# Print the updated dictionary
print("Updated Marks Dictionary:", marks)


#Task 6. Delete a key from a dictionary using del.
# Sample marks dictionary
marks = {
    "Anu": 91,
    "Banu": 92,
    "Cavin": 85
}
# Deleting the key 'Banu'
del marks["Banu"]
# Print the updated dictionary
print("Updated Marks Dictionary after deleting 'Banu':", marks)


#Task 7. Use pop() to remove a key and display the returned value.
# Sample marks dictionary
marks = {
    "Anu": 91,
    "Banu": 92,
    "Cavin": 85
}
# Using pop() to remove 'Cavin' and get her score
removed_score = marks.pop("Cavin")
# Print the returned value and the updated dictionary
print("Removed Cavin's Score:", removed_score)
print("Updated Marks Dictionary:", marks)


#Task 8. Use popitem() and explain how it works.
# Sample employees dictionary
employees = {
    "Anu": 101,
    "Banu": 102,
    "Charu": 103
}
# Use popitem() to remove and return the last inserted key-value pair
removed_item = employees.popitem()
print("Removed item:", removed_item)
print("Updated employees dictionary:", employees)


#Task 9. Clear all entries in a dictionary using clear() and show the result.
# Sample contact dictionary
contact = {
    "name": "Joseph",
    "phone": "123-456-7890",
    "email": "joseph@example.com"
}
# Clear all entries in the dictionary
contact.clear()
# Print the cleared dictionary
print("Cleared contact dictionary:", contact)

#Task 10. Check if a key exists in the dictionary using the in keyword.
# Sample marks dictionary
marks = {
     "Anu": 91,
    "Banu": 92,
    "Cavin": 85
}
# Check if 'Anu' exists in the dictionary
if "Anu" in marks:
    print("Anu is in the marks dictionary.")
else:
    print("Anu is not in the marks dictionary.")

# Check if 'Diya' exists in the dictionary
if "Diya" in marks:
    print("Diya is in the marks dictionary.")
else:
    print("Diya is not in the marks dictionary.")


##Dictionary Iteration
#Task 11. Loop through a dictionary and print all keys.
marks = {
    "Anu": 91,
    "Banu": 85,
    "Cavin": 95,
    "Diya": 78,
    "Elan": 92
}
print("All keys:")
for key in marks:
    print(key)


#Task 12. Loop through a dictionary and print all values.
marks = {
    "Anu": 91,
    "Banu": 85,
    "Cavin": 95,
    "Diya": 78,
    "Elan": 92
}
print("All values:")
for value in marks.values():
    print(value)


#Task 13. Loop through both keys and values using .items().
marks = {
    "Anu": 91,
    "Banu": 85,
    "Cavin": 95,
    "Diya": 78,
    "Elan": 92
}
print("Keys and values:")
for key, value in marks.items():
    print(f"{key}: {value}")


#Task 14. Count how many values in a dictionary are above a certain threshold (e.g., 90).
marks = {
    "Anu": 91,
    "Banu": 85,
    "Cavin": 95,
    "Diya": 78,
    "Elan": 92
}
threshold = 90
count = sum(1 for v in marks.values() if v > threshold)
print(f"Number of values above {threshold}:", count)


#Task 15. Create a function that returns all keys that have a specific value.
marks = {
    "Anu": 91,
    "Banu": 85,
    "Cavin": 95,
    "Diya": 78,
    "Elan": 92
}
def keys_with_value(d, val):
    return [k for k, v in d.items() if v == val]
target_value = 91
keys_found = keys_with_value(marks, target_value)
print(f"Keys with value {target_value}:", keys_found)

##Dictionary Methods
#Task 16. Use update() to merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print("Merged dictionary using update():", dict1)


#Task 17. Use setdefault() to add a key only if it doesn't exist.
student = {"name": "John", "age": 20}
student.setdefault("grade", "A")  # Adds 'grade' since it doesn't exist
student.setdefault("age", 21)     # Does NOT update 'age' because it exists
print("17. Dictionary after setdefault():", student)


#Task 18. Use copy() to duplicate a dictionary, then prove they are separate.
original = {"x": 10, "y": 20}
duplicate = original.copy()
duplicate["x"] = 99
print("18. Original dictionary:", original)
print("18. Copied dictionary after modification:", duplicate)


#Task 19. Create a dictionary using dict() constructor from a list of tuples.
tuple_list = [("key1", "value1"), ("key2", "value2")]
constructed_dict = dict(tuple_list)
print("19. Dictionary created from list of tuples:", constructed_dict)


#Task 20. Get a list of all keys using .keys() and all values using .values().
sample_dict = {"a": 1, "b": 2, "c": 3}
keys = list(sample_dict.keys())
values = list(sample_dict.values())
print("20. List of keys:", keys)
print("20. List of values:", values)


##Practical Use Cases
#Task 21. Create a shopping cart dictionary: item name as key, quantity as value.
shopping_cart = {
    "apples": 4,
    "bananas": 6,
    "bread": 2,
    "milk": 1
}
print("Shopping Cart:", shopping_cart)


#Task 22. Build a grade book dictionary with student names and their grades.
grade_book = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-",
    "Diana": "B"
}
print("Grade Book:", grade_book)


#Task 23. Make a phonebook dictionary and search for a contact.
phonebook = {
    "John Doe": "555-1234",
    "Jane Smith": "555-5678",
    "Emily Davis": "555-8765"
}
search_name = "Jane Smith"
phone = phonebook.get(search_name, "Contact not found")
print(f"Phone number for {search_name}:", phone)


#Task 24. Develop a product inventory system where product ID is the key and stock info is the value.
inventory = {
    101: {"name": "Laptop", "stock": 10},
    102: {"name": "Mouse", "stock": 25},
    103: {"name": "Keyboard", "stock": 15}
}
print("Inventory:", inventory)


#Task 25. Track attendance using a dictionary with dates as keys and list of students as values.
attendance = {
    "2025-07-14": ["Alice", "Bob", "Charlie"],
    "2025-07-15": ["Alice", "Diana"],
    "2025-07-16": ["Bob", "Charlie", "Diana"]
}
print("Attendance records:", attendance)


##Nested Dictionaries
#Task 26. Create a nested dictionary for employees: {emp_id: {"name":..., "salary":...}}
employees = {
    1001: {"name": "Anu", "salary": 70000},
    1002: {"name": "Banu", "salary": 65000},
    1003: {"name": "Charu", "salary": 72000}
}
print("Employees Nested Dictionary:", employees)


#Task 27. Access a nested value from the above dictionary.
banu_salary = employees[1002]["salary"]
print("Banu's Salary:", banu_salary)


#Task 28. Add a new employee to the nested dictionary.
employees[1004] = {"name": "Diya", "salary": 68000}
print("Added Diya:", employees)


#Task 29. Update only the salary of a specific employee in the nested dictionary.
employees[1001]["salary"] = 75000
print("Updated Anu's Salary:", employees)


#Task 30. Loop through the nested dictionary and print employee name and salary.
print("Employee Names and Salaries:")
for emp_id, info in employees.items():
    print(f"ID: {emp_id}, Name: {info['name']}, Salary: ${info['salary']}")


##Dictionary Comprehension
#Task 31. Generate a dictionary of squares: {n: n**2 for n in range(1, 6)}
squares = {n: n**2 for n in range(1, 6)}
print("Squares Dictionary:", squares)


#Task 32. Create a dictionary from a list of numbers where values are "even"/"odd".
numbers = [1, 2, 3, 4, 5, 6]
even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in numbers}
print("Even/Odd Dictionary:", even_odd)


#Task 33. Convert a list of words into a dictionary with word as key and length as value.
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print("Word Lengths Dictionary:", word_lengths)


#Task 34. Swap keys and values in a dictionary using comprehension.
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("Swapped Dictionary:", swapped)


#Task 35. Filter a dictionary to retain only items with values greater than a threshold.
data = {"x": 5, "y": 15, "z": 10}
threshold = 8
filtered = {k: v for k, v in data.items() if v > threshold}
print(f"Filtered Dictionary (values > {threshold}):", filtered)


##Data Processing
#Task 36. Count the frequency of each character in a given string using a dictionary.
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
sample_string = "hello world"
print("Character Frequency:", char_frequency(sample_string))


#Task 37. Create a word count dictionary from a paragraph.
def word_count(paragraph):
    words = paragraph.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

paragraph = "This is a test. This test is only a test."
print("Word Count:", word_count(paragraph))


#Task 38. Create a dictionary to store fruit prices and find the most expensive fruit.
fruit_prices = {
    "apple": 1.2,
    "banana": 0.5,
    "cherry": 2.5,
    "date": 3.0
}
most_expensive = max(fruit_prices, key=fruit_prices.get)
print("Most Expensive Fruit:", most_expensive, "at $", fruit_prices[most_expensive])


#Task 39. Calculate total value of inventory using product price and quantity dictionaries.
prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5}
quantities = {"apple": 10, "banana": 20, "cherry": 5}
total_value = sum(prices[item] * quantities.get(item, 0) for item in prices)
print("Total Inventory Value:", total_value)


#Task 40. Group a list of students by grade into a dictionary.
from collections import defaultdict
students = [
    ("Anu", "A"),
    ("Banu", "B"),
    ("Charu", "C"),
    ("Diya", "C"),
    ("Elan", "A")
]
grade_groups = defaultdict(list)
for student, grade in students:
    grade_groups[grade].append(student)
print("Students Grouped by Grade:", dict(grade_groups))


##Advanced Applications
#Task 41. Implement a caching system using a dictionary to store function results.
# Function with manual caching using a dictionary
cache = {}
def expensive_computation(x):
    if x in cache:
        print("Fetching from cache...")
        return cache[x]
    print("Computing...")
    result = x * x  # Simulate a costly operation
    cache[x] = result
    return result
print("Caching System:")
print(expensive_computation(5))  # Computes and caches
print(expensive_computation(5))  # Uses cache


#Task 42. Simulate a URL shortening service using dictionaries.
# URL Shortener
url_map = {}
short_map = {}
def shorten_url(long_url):
    short = f"url{len(url_map)+1}"
    url_map[short] = long_url
    short_map[long_url] = short
    return short
def expand_url(short_url):
    return url_map.get(short_url, "URL not found")
print("URL Shortener:")
short = shorten_url("https://example.com/very-long-url")
print("Shortened:", short)
print("Expanded:", expand_url(short))


#Task 43. Build a language translator using a dictionary (English → Tamil).
from indictrans2 import IndicTranslator
# Create a translator instance
translator = IndicTranslator()
def translate_to_tamil(text: str) -> str:
    """
    Translate the given English text to Tamil.
    Automatically detects source language if needed.
    """
    return translator.translate(text, target_lang="ta")
# Example usage
if __name__ == "__main__":
    sentences = [
        "Hello, how are you?",
        "Thank you for your help!",
        "This is a language translator."
    ]
    for s in sentences:
        print(f"EN: {s}")
        print(f"TA: {translate_to_tamil(s)}\n")


#Task 44. Simulate a login system where usernames and passwords are stored in a dictionary.
# Simple login system
users = {
    "admin": "admin123",
    "jack": "pass456",
    "annie": "anniepwd"
}
def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    return "Invalid username or password"
print("Login System:")
print(login("jack", "pass456"))       # Success
print(login("jack", "wrongpass"))     # Failure


#Task 45. Develop a movie collection manager where movie title is key and info like (year, genre) is the value.
# Movie collection
movies = {
    "Inception": {"year": 2010, "genre": "Sci-Fi"},
    "Titanic": {"year": 1997, "genre": "Romance"},
    "Interstellar": {"year": 2014, "genre": "Sci-Fi"}
}
def add_movie(title, year, genre):
    movies[title] = {"year": year, "genre": genre}
def get_movie(title):
    return movies.get(title, "Movie not found")
print("\n45. Movie Collection:")
add_movie("The Matrix", 1999, "Sci-Fi")
print("Get 'Inception':", get_movie("Inception"))
print("Get 'The Matrix':", get_movie("The Matrix"))


##Utility Tools
#Task 46. Create a dictionary-based simple calculator (keys as operators and values as functions).
# Define calculator operations
calculator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Division by zero"
}
# Example usage
op = '+'
x, y = 10, 5
result = calculator[op](x, y)
print(f"{x} {op} {y} = {result}")

#Task 47. Build a travel expense tracker using a dictionary where destinations are keys and costs are values.
travel_expenses = {
    "Paris": 1200,
    "London": 980,
    "Tokyo": 1500
}
# Add an expense
travel_expenses["Dubai"] = 1100
# Calculate total expense
total = sum(travel_expenses.values())
print("Travel Expenses:", travel_expenses)
print("Total:", total)


#Task 48. Develop a file extension counter: count how many files per extension from a list of filenames.
from collections import defaultdict
filenames = [
    "report.docx", "image.png", "notes.txt", "data.csv",
    "photo.png", "summary.docx", "script.py", "table.csv"
]
ext_count = defaultdict(int)
for file in filenames:
    ext = file.split('.')[-1]
    ext_count[ext] += 1
print("File Extension Count:", dict(ext_count))


#Task 49. Build a dictionary that maps countries to their capital cities and allow searching.
countries = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "Canada": "Ottawa"
}
# Search for a capital
country = "Japan"
capital = countries.get(country, "Country not found")
print("Capital of", country, "is", capital)


#Task 50. Create a quiz app using dictionaries: {question: correct_option} and verify answers.
quiz = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky on a clear day?": "Blue"
}

# Simulated user answers
user_answers = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky on a clear day?": "Green"
}

# Evaluate
score = 0
print("Quiz Results:")
for question, correct in quiz.items():
    user_ans = user_answers.get(question, "")
    result = "✅" if user_ans.lower() == correct.lower() else "❌"
    print(f"{question}\n  Your answer: {user_ans} ({result})")
    if result == "✅":
        score += 1

print(f"\nFinal Score: {score} / {len(quiz)}")
