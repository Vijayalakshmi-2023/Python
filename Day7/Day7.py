##SECTION 1: Creating and Accessing Strings (1–10)
#Task1: ✅ Create a string using single quotes, double quotes, and triple quotes.
# Using all types of quotes in a single program
single_quote_str = 'This is a string in single quotes'
double_quote_str = "This is a string in double quotes"
triple_quote_str = '''This is a string in triple quotes.
It can span multiple lines.'''
# You can also embed quotes inside each other:
mixed_quote_str = 'She said, "It\'s a beautiful day!"'
# Printing all
print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)
print(mixed_quote_str)
complex_str = """This string contains 'single quotes', "double quotes", and is defined using triple quotes."""
print(complex_str)


#Task2: ✅ Create a multiline quote using triple quotes and print it.
multiline_quote = """Success is not final,
failure is not fatal:
It is the courage to continue that counts.
- Winston Churchill"""
print(multiline_quote)


#Task3: ✅ Access the first and last characters from a string using positive and negative indexing.
my_name = "Vijayalakshmi!"
# Accessing the first character using positive indexing
first_char = my_name[0]
# Accessing the last character using negative indexing
last_char = my_name[-1]
print("First character:", first_char)
print("Last character:", last_char)


#Task4: ✅ Write a program to print every character in a string using a for loop.
# Define the string
name = "Vijayalakshmi"
# Loop through each character in the string
for character in name:
    print(character)

#Task5: ✅ Slice a string to extract only the middle 3 characters.
name = "Vijayalakshmi"
mid_index = len(name) // 2
middle_three = name[mid_index - 1 : mid_index + 2]
print("Original string:", name)
print("Middle 3 characters:", middle_three)


#Task6: ✅ Access and print every second character from a string using slicing.
name = "Vijayalakshmi Nagarajan"
# Slice to get every second character
every_second_char = name[::2]
print("Original string:", name)
print("Every second character:", every_second_char)


#Task7: ✅ Print all vowels in a given string using indexing and conditions.
name = "Vijayalakshmi"
vowels = "aeiouAEIOU"
print("Vowels in the string:")
for i in range(len(name)):
    char = name[i]
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' \
       or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print(char)

#Task8: ✅ Extract the domain from an email like "user@gmail.com" using slicing.
email = "vlakshmin2023@gmail.com"
# Find the index of '@'
at_index = email.index('@')
# Slice the domain part
domain = email[at_index + 1:]
print("Email:", email)
print("Domain:", domain)

#Task9: ✅ Check whether the first and last characters of a string are the same.
name = "Vijayalakshmi"
# Check if string is not empty
if len(name) > 0 and name[0] == name[-1]:
    print("The first and last characters are the same.")
else:
    print("The first and last characters are different.")


#Task10: ✅ Print the reverse of a string using slicing.
name = "Vijayalakshmi"
# Reverse the string using slicing
reversed_name = name[::-1]
print("Original string:", name)
print("Reversed string:", reversed_name)

##🟦 SECTION 2: Immutability and Modification (11–15)
#Task 11: ❌ Try to modify a single character in a string (to understand immutability).
text = "Hello"
# This will raise an error because strings are immutable
# text[0] = 'H'  # ❌ Uncommenting this will cause: TypeError
print("Strings are immutable — you can't assign to text[0].")


#Task 12:✅ Write code to change the first character of a string using slicing and concatenation.
text = "hello"
modified = 'H' + text[1:]
print("Original:", text)
print("Modified:", modified)


#Task 13:✅ Replace a character in the middle of a string by reconstructing it.
text = "hello"
index = 2  # index of the character 'l'
new_char = 'X'
modified = text[:index] + new_char + text[index + 1:]
print("Original:", text)
print("Modified:", modified)


#Task 14:✅ Create a function that replaces all vowels in a string with '*'.
def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result
# Example usage
text = "Programming is fun"
print("Original:", text)
print("Vowels replaced:", replace_vowels(text))


#Task 15:✅ Create a function that returns a new string by replacing all occurrences of 'a' with '@'.
def replace_a_with_at(s):
    return s.replace('a', '@')
# Example usage
text = "A cat and a bat"
print("Original:", text)
print("Modified:", replace_a_with_at(text))

##🟦 SECTION 3: Deleting and Updating Strings (16–20)
#Task 16:✅ Create a string and delete it using del, then try to print it (catch the error).
try:
    message = "This string will be deleted"
    del message  # Deletes the variable
    print(message)  # Trying to access it will raise NameError
except NameError as e:
    print("Error:", e)


#Task 17:✅ Concatenate two strings using + and print the result.
first = "Hello"
second = "World"
combined = first + " " + second
print("Concatenated string:", combined)


#Task 18:✅ Write a program that takes a name and appends "Welcome!" to it.
name = "Alice"
welcome_message = name + ", Welcome!"
print(welcome_message)


#Task 19:✅ Take user input and create a new sentence by combining it with a fixed phrase.
user_input = input("Enter your favorite hobby: ")
sentence = "That's great! " + user_input + " sounds fun."
print(sentence)


#Task 20:✅ Repeat the word "Hello" 5 times using the * operator.
greeting = "Hello " * 5
print(greeting.strip())  # strip() removes the trailing space


##🟦 SECTION 4: Common String Methods (21–35)
#Task 21:✅ Use len() to count the characters in a string.
text = "Hello World"
print("Length:", len(text))


#Task 22:✅ Convert a string to lowercase using .lower().
text = "PYTHON"
print("Lowercase:", text.lower())


#Task 23:✅ Convert a string to uppercase using .upper().
text = "python"
print("Uppercase:", text.upper())
  

#Task 24:✅ Remove leading and trailing whitespaces using .strip().
text = "   hello world   "
print("Stripped:", text.strip())


#Task 25:✅ Use .replace() to change "bad" to "good" in a sentence.
sentence = "This is a bad idea."
print(sentence.replace("bad", "good"))


#Task 26:✅ Split a comma-separated string into a list using .split(',').
csv = "apple,banana,cherry"
fruits = csv.split(',')
print(fruits)


#Task 27:✅ Join a list of words with - using .join().
words = ["python", "is", "fun"]
joined = "-".join(words)
print(joined)


#Task 28:✅ Count how many times "a" appears in "banana" using .count().
text = "banana"
print("Count of 'a':", text.count("a"))


#Task 29:✅ Use .find() to get the first index of the letter 'o' in "Google".
text = "Google"
print("First 'o' at index:", text.find('o'))


#Task 30:✅ Create a program to convert 'Python is FUN' to 'python-is-fun'.
text = "Python is FUN"
converted = text.lower().replace(" ", "-")
print(converted)


#Task 31:✅ Write a function that counts vowels and consonants in a string.
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

# Example
vowels, consonants = count_vowels_consonants("Python Programming")
print("Vowels:", vowels)
print("Consonants:", consonants)


#Task 32:✅ Use .replace() to remove all spaces from a string.
text = "remove all spaces"
no_spaces = text.replace(" ", "")
print(no_spaces)


#Task 33:✅ Use .split() and a for loop to print each word on a new line.
text = "Split this sentence into words"
words = text.split()
for word in words:
    print(word)


#Task 34:✅ Print the middle character of a string (if odd length).
text = "abcde"
if len(text) % 2 != 0:
    middle_char = text[len(text) // 2]
    print("Middle character:", middle_char)
else:
    print("String length is even, no single middle character.")


#Task 35:✅ Write a function that returns the first and last characters combined.
def first_and_last(s):
    if len(s) == 0:
        return ""
    return s[0] + s[-1]
# Example
result = first_and_last("Python")
print("First and last combined:", result)


##🟦 SECTION 5: Concatenation and Repetition (36–40)
#Task 36:✅ Concatenate first name and last name with a space in between.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)


#Task 37:✅ Write a program that asks for a name and prints it 3 times using *.
name = input("Enter your name: ")
print((name + " ") * 3)


#Task 38:✅ Create a sentence by joining five different words using +.
word1 = "Learning"
word2 = "Python"
word3 = "is"
word4 = "fun"
word5 = "everyday."
sentence = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5
print(sentence)


#Task 39:✅ Use .join() to combine a list of characters into a word.
chars = ['c', 'o', 'd', 'e']
word = ''.join(chars)
print("Joined word:", word)


#Task 40:✅ Take user input for a name and print “Welcome <name>” using string concatenation.
name = input("Enter your name: ")
welcome = "Welcome " + name
print(welcome)

##🟦 SECTION 6: String Formatting (41–50)
#Task 41:✅ Use f-string to print “My name is John and I am 30 years old.”
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


#Task 42:✅ Use .format() to insert 2 numbers and print their sum.
num1 = 10
num2 = 20
print("The sum of {} and {} is {}".format(num1, num2, num1 + num2))


#Task 43:✅ Use % formatting to display the price of a product: "%s costs ₹%.2f"
product = "Watch"
price = 499.999
print("%s costs ₹%.2f" % (product, price))


#Task 44:✅ Create a function that takes name and marks and prints a result using all 3 formatting methods.
def print_result(name, marks):
    # f-string
    print(f"{name} scored {marks} marks.")
    # .format()
    print("{} got {} marks.".format(name, marks))
    # % formatting
    print("%s has secured %d marks." % (name, marks))
# Example
print_result("Alice", 85)


#Task 45:✅ Format a list of products and their prices into a formatted table using f-strings.
products = [("Pen", 10), ("Notebook", 50), ("Eraser", 5)]

print(f"{'Product':<10} {'Price (₹)':>10}")
print("-" * 22)
for item, price in products:
    print(f"{item:<10} ₹{price:>9.2f}")


#Task 46:✅ Ask for user input (name, age) and print using .format().
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, {}. You are {} years old.".format(name, age))


#Task 47:✅ Print temperature conversion: "Temperature is 35°C or 95°F" using f-string.
celsius = 35
fahrenheit = celsius * 9/5 + 32
print(f"Temperature is {celsius}°C or {fahrenheit}°F")


#Task 48:✅ Format a sentence where the price changes dynamically: "The discounted price is ₹999"
discounted_price = 999
print(f"The discounted price is ₹{discounted_price}")


#Task 49:✅ Write a function that accepts employee details and formats them using f-string.
def employee_info(name, id, dept, salary):
    print(f"Employee: {name} | ID: {id} | Department: {dept} | Salary: ₹{salary:.2f}")
# Example
employee_info("Ravi", "E102", "IT", 55000.75)


#Task 50:✅ Create a dynamic weather report sentence using all formatting styles.
def weather_report(city, temp_c, humidity):
    temp_f = temp_c * 9/5 + 32
    # f-string
    print(f"Weather in {city}: {temp_c}°C / {temp_f}°F")
    # .format()
    print("Humidity is {}% in {}.".format(humidity, city))
    # % formatting
    print("Current temperature: %.1f°C" % temp_c)
# Example
weather_report("Mumbai", 32.5, 78)

