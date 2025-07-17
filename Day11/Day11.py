##Creating and Accessing Sets
#Task 1. Create a set of favorite fruits and print it.
favorite_fruits = {"apple", "banana", "mango", "grape"}
print("Favorite Fruits:", favorite_fruits)

#Task 2. Convert a list with duplicate values into a unique set.
fruit_list = ["apple", "banana", "apple", "orange", "banana"]
unique_fruits = set(fruit_list)
print("Unique Fruits:", unique_fruits)

#Task 3. Check if a given item exists in a set using the 'in' keyword.
item_to_check = "banana"
if item_to_check in unique_fruits:
    print(f"{item_to_check} is in the set.")
else:
    print(f"{item_to_check} is not in the set.")

#Task 4. Create a set from a string and print all unique characters.
sample_string = "hello world"
unique_chars = set(sample_string)
print("Unique characters in string:", unique_chars)

#Task 5. Iterate through a set and print each element.
print("Iterating through favorite fruits:")
for fruit in favorite_fruits:
    print(fruit)


##Adding Elements
#Task 6. Create an empty set and add five movie names using add().
movies = set()
movies.add("Inception")
movies.add("The Matrix")
movies.add("Interstellar")
movies.add("Parasite")
movies.add("The Dark Knight")
print("Movies Set:", movies)

#Task 7. Add multiple subjects to a set using update() from a list.
subjects = {"Math", "English"}
more_subjects = ["Science", "History", "Geography"]
subjects.update(more_subjects)
print("Subjects Set:", subjects)

#Task 8. Add multiple letters from a string into a set using update().
letters_set = set()
letters_set.update("education")
print("Letters Set from String:", letters_set)


##Removing Elements
#Task 9. Remove a specific city from a set using remove().
cities = {"New York", "London", "Tokyo", "Paris"}
cities.remove("Tokyo")  # Will raise an error if "Tokyo" is not present
print("Cities after removing Tokyo:", cities)

#Task 10. Try to remove an element using discard() and avoid an error if not present.
cities.discard("Berlin")  # No error even though "Berlin" isn't in the set
print("Cities after discarding Berlin (if present):", cities)

#Task 11. Remove a random item from a set using pop() and print it.
removed_city = cities.pop()  # Removes and returns a random element
print("Randomly removed city:", removed_city)
print("Cities after pop():", cities)

#Task 12. Clear all elements from a set using clear() and check if it is empty.
cities.clear()
print("Cities after clear():", cities)
print("Is the set empty?", len(cities) == 0)


##Set Operations
#Task 13. Find the union of two sets of programming languages.
languages1 = {"Python", "Java", "C++"}
languages2 = {"Ruby", "JavaScript", "Python"}
union_languages = languages1 | languages2  # or languages1.union(languages2)
print("Union of Programming Languages:", union_languages)

#Task 14. Find the intersection of two sets of sports.
sports1 = {"Soccer", "Tennis", "Cricket", "Basketball"}
sports2 = {"Baseball", "Cricket", "Tennis"}
common_sports = sports1 & sports2  # or sports1.intersection(sports2)
print("Common Sports (Intersection):", common_sports)

#Task 15. Find the difference between set A and set B (A - B).
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
difference = A - B  # or A.difference(B)
print("Difference (A - B):", difference)

#Task 16. Find the symmetric difference (items in either set, but not both).
sym_diff = A ^ B  # or A.symmetric_difference(B)
print("Symmetric Difference (A ^ B):", sym_diff)

#Task 17. Perform chained operations like (A | B) - (A & B).
chained_result = (A | B) - (A & B)
print("Chained Operation Result ((A | B) - (A & B)):", chained_result)


##Set Relationships
#Task 18. Check if a set of backend skills is a subset of full-stack skills.
backend_skills = {"Python", "Django", "SQL"}
fullstack_skills = {"HTML", "CSS", "JavaScript", "Python", "Django", "SQL"}
is_subset = backend_skills.issubset(fullstack_skills)
print("Is backend a subset of full-stack?", is_subset)

#Task 19. Verify if a set of developers is a superset of testers.
developers = {"Alice", "Bob", "Charlie", "Diana"}
testers = {"Bob", "Diana"}
is_superset = developers.issuperset(testers)
print("Are developers a superset of testers?", is_superset)

#Task 20. Determine if two sets of colors are disjoint (no common elements).
colors1 = {"red", "green", "blue"}
colors2 = {"yellow", "purple", "orange"}
are_disjoint = colors1.isdisjoint(colors2)
print("Are colors1 and colors2 disjoint?", are_disjoint)

#Task 21. Use multiple sets to test all subset-superset combinations.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7}

print("set1 is subset of set2:", set1.issubset(set2))
print("set2 is superset of set1:", set2.issuperset(set1))
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))

#Task 22. Real-life case of issubset() using required course completions.
required_courses = {"Math", "Science", "English"}
student_courses = {"Math", "Science", "English", "History"}
has_completed_requirements = required_courses.issubset(student_courses)
print("Has the student completed all required courses?", has_completed_requirements)


##Working with copy()
#Task 23: Create a backup of a set using copy() and show that modifying the copy doesn’t affect the original.
gadgets = {"laptop", "smartphone", "tablet"}
gadgets_backup = gadgets.copy()
gadgets_backup.add("smartwatch")
print("Original gadgets set:", gadgets)
print("Modified backup set:", gadgets_backup)


##Frozen Set Tasks
#Task 24: Create a frozenset of vowels and demonstrate immutability.
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
print("Frozenset of vowels:", vowels)

#Task 25: Try to add an element to a frozenset and catch the error gracefully.
try:
    vowels.add('y')  # This will raise an AttributeError
except AttributeError as e:
    print("Error: Cannot modify a frozenset -", e)

#Task 26: Use a frozenset as a key in a dictionary for caching purposes.
cache = {}
key = frozenset(["user_id", "session_token"])
cache[key] = "Cached session data"
print("Cache with frozenset key:", cache)


##Set Comprehension
#Task 27: Generate a set of even numbers from 1 to 20 using set comprehension.
even_numbers = {x for x in range(1, 21) if x % 2 == 0}
print("Even numbers (1–20):", even_numbers)

#Task 28: Generate a set of unique lowercase characters from a sentence using set comprehension.
sentence = "Set comprehensions are powerful in Python!"
lower_chars = {char for char in sentence if char.islower()}
print("Unique lowercase letters:", lower_chars)

#Task 29: Create a set of squares for numbers 1 to 10 using set comprehension.
squares = {x**2 for x in range(1, 11)}
print("Squares from 1 to 10:", squares)

#Task 30: Use a set comprehension to filter out vowels from a sentence.
sentence = "This is a demonstration of set comprehension!"
vowels = {'a', 'e', 'i', 'o', 'u'}
non_vowel_chars = {char for char in sentence if char.lower() not in vowels and char.isalpha()}
print("Non-vowel characters:", non_vowel_chars)


##Real-World Simulations
#Task 31. Store a list of registered users and block users, then find the allowed users using set difference.
registered_users = {"alice", "bob", "charlie", "diana"}
blocked_users = {"bob", "diana"}
allowed_users = registered_users - blocked_users
print("Allowed users:", allowed_users)

#Task 32. Use sets to find students enrolled in both Python and Java courses (intersection).
python_students = {"emma", "liam", "olivia", "noah"}
java_students = {"olivia", "liam", "ava"}
both_courses = python_students & java_students
print("Students in both Python and Java:", both_courses)


#Task 33. Compare two sets of stock symbols to find new listings (difference).
existing_stocks = {"AAPL", "GOOGL", "AMZN", "TSLA"}
today_stocks = {"AAPL", "GOOGL", "AMZN", "TSLA", "NVDA", "BABA"}
new_listings = today_stocks - existing_stocks
print("New stock listings:", new_listings)


#Task 34. Track users who logged in either yesterday or today (union).
yesterday_logins = {"alice", "bob", "charlie"}
today_logins = {"charlie", "diana", "emma"}
all_logins = yesterday_logins | today_logins
print("Total unique users who logged in:", all_logins)
 

#Task 35. Identify users who changed passwords on only one of the two days (symmetric difference).
day1_changes = {"alice", "charlie", "emma"}
day2_changes = {"charlie", "bob", "frank"}
changed_once = day1_changes ^ day2_changes
print("Users who changed password on only one day:", changed_once)


#Task 36. Detect duplicate entries in a list of product SKUs using sets.
product_skus = ["SKU1", "SKU2", "SKU3", "SKU2", "SKU4", "SKU3"]
unique_skus = set()
duplicates = set()
for sku in product_skus:
    if sku in unique_skus:
        duplicates.add(sku)
    else:
        unique_skus.add(sku)
print("Duplicate SKUs found:", duplicates)

#Task 37. Create a set from a CSV file’s column and count unique entries.
# Simulating reading from a CSV column (e.g., 'Country')
csv_column_data = ["USA", "Canada", "USA", "Mexico", "Canada", "Brazil"]
unique_countries = set(csv_column_data)
print("Unique countries:", unique_countries)
print("Count of unique countries:", len(unique_countries))


#Task 38. Build a unique tag manager system for blog posts using sets.
post_tags = [
    {"python", "web", "tutorial"},
    {"web", "html", "css"},
    {"python", "data", "machine learning"},
]
all_tags = set()
for tags in post_tags:
    all_tags.update(tags)
print("All unique blog tags:", all_tags)

#Task 39. Check if a given list of security permissions is covered by the default permission set.
default_permissions = {"read", "write", "execute", "delete"}
user_required_permissions = {"read", "write"}
is_covered = user_required_permissions.issubset(default_permissions)
print("Are all user permissions covered?", is_covered)


##Combination Tasks
#Task 40. Create two sets from random numbers and apply all operations: union, intersection, etc.
import random
set_a = {random.randint(1, 20) for _ in range(10)}
set_b = {random.randint(10, 30) for _ in range(10)}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

#Task 41. Build a contact manager that stores unique email addresses using a set.
contacts = set()
contacts.update(["alice@example.com", "bob@example.com", "alice@example.com"])  # duplicate ignored
print("Unique email contacts:", contacts)

#Task 42. Store completed achievements of players and check who earned all major trophies.
major_trophies = {"MVP", "Top Scorer", "Champion"}
player_achievements = {
    "Alice": {"MVP", "Champion", "Top Scorer"},
    "Bob": {"Champion", "Top Scorer"},
}
for player, trophies in player_achievements.items():
    has_all = major_trophies.issubset(trophies)
    print(f"{player} earned all major trophies? {has_all}")

#Task 43. Keep track of unique IPs from a server log using a set.
server_logs = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "10.0.0.1"]
unique_ips = set(server_logs)
print("Unique IP addresses:", unique_ips)


#Task 44. Extract unique hashtags from a list of tweets using sets.
tweets = [
    "Learning #Python is fun! #coding",
    "#AI is the future. #Python",
    "Explore #MachineLearning and #AI",
]
hashtags = set()
for tweet in tweets:
    hashtags.update({word for word in tweet.split() if word.startswith("#")})
print("Unique hashtags:", hashtags)

#Task 45. Track unique book titles from multiple libraries using update().
library1 = {"1984", "Brave New World", "Fahrenheit 451"}
library2 = {"1984", "Dune", "Foundation"}
library3 = {"Neuromancer", "Foundation", "Dune"}
all_books = set()
all_books.update(library1, library2, library3)
print("All unique book titles:", all_books)


#Task 46. Validate if all required modules are installed using issubset() on installed_modules.
installed_modules = {"numpy", "pandas", "matplotlib", "scikit-learn"}
required_modules = {"numpy", "pandas"}
is_valid = required_modules.issubset(installed_modules)
print("All required modules installed?", is_valid)


##Edge Case Handling
#Task 47. Try removing a non-existent item using remove() and handle the exception.
fruits = {"apple", "banana", "cherry"}
try:
    fruits.remove("orange")  # "orange" is not in the set
except KeyError:
    print("Error: 'orange' not found in the set.")
print("Current fruits set:", fruits)

#Task 48. Explain the difference between remove() and discard() using a test set.
test_set = {"apple", "banana", "cherry"}
test_set.remove("banana")
print("After remove('banana'):", test_set)
test_set.discard("apple")
print("After discard('apple'):", test_set)
try:
    test_set.remove("orange")
except KeyError:
    print("remove() raised KeyError because 'orange' is not in the set.")
test_set.discard("orange")
print("discard() did not raise an error when removing 'orange'.")

#Task 49. Create a set from a list with mixed datatypes and remove all integers using set comprehension.
mixed_list = [1, "apple", 2.5, 3, "banana", 4, 5.5, "cherry"]
filtered_set = {item for item in set(mixed_list) if not isinstance(item, int)}
print("Set without integers:", filtered_set)

#Task 50. Create a set of characters from a multiline text, excluding punctuation.
import string
multiline_text = """
Hello, world!
Welcome to the set operations tutorial.
Let's learn about Python sets.
"""
clean_text = ''.join(ch for ch in multiline_text if ch not in string.punctuation and not ch.isspace())
char_set = set(clean_text)
print("Unique characters (excluding punctuation):", char_set)
