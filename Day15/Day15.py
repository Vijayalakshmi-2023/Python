##Basic Exception Handling (1–10)
#Task 1:
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")


#Task 2:
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("Invalid age input:", e)


#Task 3:
try:
    filename = input("Enter the filename to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")


#Task 4:
try:
    f = open("sample.txt", "w")
    f.close()
    print(f.read())  # reading from closed file
except ValueError:
    print("Error: Cannot read from a closed file.")

#Task 5:
try:
    my_list = ['apple', 'banana', 'cherry']
    print("List items:", my_list)
    index = int(input("Enter an index (0 to 2): "))
    print("Item at index", index, "is:", my_list[index])
except IndexError:
    print("Error: Index out of range. Please enter a valid index.")
except ValueError:
    print("Error: Please enter a valid integer.")

#Task 6:
try:
    my_dict = {'a': 1, 'b': 2}
    key = input("Enter dictionary key (a/b): ")
    print("Value:", my_dict[key])
except KeyError:
    print("Error: Key not found in dictionary.")

#Task 7:
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Not a valid integer.")

#Task 8:
try:
    print("abc" + 5)
except TypeError:
    print("Error: Cannot add string and integer.")

#Task 9:
try:
    my_str = "hello"
    my_str.fake_method()
except AttributeError:
    print("Error: Method does not exist.")

#Task 10:
try:
    print(undefined_variable)
except NameError:
    print("Error: Variable is not defined.")

##Multiple Except, Else, Finally Blocks (11–20)
#Task 11:
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
except ValueError:
    print("Invalid input! Please enter integers.")
else:
    print("Division result:", a / b)

#Task 12:
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("That's not a number.")
finally:
    print("Done")  # Always executes

#Task 13:
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print("Result:", x / y)
except ValueError:
    print("Input must be an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Task 14:
try:
    print(10 / 0)  # Raises ZeroDivisionError
finally:
    print("This will print even if the exception is uncaught.")

# After this, the program crashes because the error isn't caught

#Task 15:
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("Valid number:", x)
finally:
    print("This runs no matter what.")

#Task 16:
try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    try:
        f.close()
        print("File closed.")
    except NameError:
        print("File was never opened.")

#Task 17:
try:
    x = int(input("Enter a number: "))
    try:
        result = 100 / x
        print("100 divided by", x, "is", result)
    except ZeroDivisionError:
        print("Inner block: Cannot divide by zero.")
except ValueError:
    print("Outer block: Invalid number.")

#Task 18:
try:
    lst = [1, 2, 3]
    idx = int(input("Enter index: "))
    print("Item:", lst[idx])
except ValueError:
    print("Please enter a number.")
except IndexError:
    print("Index out of range.")

#Task 19:
try:
    a = "text" + 5  # TypeError
except Exception as e:
    print("An unexpected error occurred:", e)

#Task 20:
#Incorrect Nesting:
try:
    print("Start")
except ValueError:
    print("Value error")
finally:
    print("Done")  # ❌ IndentationError or unreachable

#Correct Nesting:
try:
    print("Start")
except ValueError:
    print("Value error")
finally:
    print("Done")  # ✅ Proper indentation and placement


##Raise Statement (21–30)
#Task 21:
num = int(input("Enter a positive number: "))
if num < 0:
    raise ValueError("Number cannot be negative.")
print("You entered:", num)

#Task 22:
def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    print("Hello,", name)

greet("Alice")  # ✅ Works
# greet(123)    # ❌ Raises TypeError

#Task 23:
def square(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return n * n

print(square(5))  # ✅
# print(square(-2))  # ❌ Raises ValueError

#Task 24:
def login(username, password):
    correct_password = "secret123"
    if password != correct_password:
        raise Exception("Incorrect password!")
    print(f"Welcome, {username}!")

# login("admin", "wrong")  # ❌
login("admin", "secret123")  # ✅

#Task 25:
data = {"name": "Alice", "age": 25}

if "email" not in data:
    raise KeyError("Missing required key: 'email'")

#Task 26:
x = 10
y = 0
if y == 0:
    raise ZeroDivisionError("Cannot divide by zero. Please provide a non-zero denominator.")
print(x / y)

#Task 27:
num = int(input("Enter an even number: "))
assert num % 2 == 0, "The number is not even."
print("Even number:", num)

#Task 28:
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    print("Email is valid.")

# validate_email("test@example.com")  # ✅
# validate_email("invalid-email")     # ❌ Raises ValueError

#Task 29:
my_list = []

if not my_list:
    raise Exception("List is empty. Cannot process.")
print("First item:", my_list[0])

#Task 30:
try:
    with open("sample.txt", "r") as f:
        content = f.read()
        if not content.strip():
            raise Exception("File is empty.")
        print(content)
except FileNotFoundError:
    print("File not found.")


##Custom/User-Defined Exceptions (31–40)
#Task 31:
class NegativeNumberError(Exception):
    pass
num = int(input("Enter a positive number: "))
if num < 0:
    raise NegativeNumberError("Number cannot be negative.")
print("Number:", num)

#Task 32:
class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))
if age < 0 or age > 150:
    raise InvalidAgeError("Age must be between 0 and 150.")
print("Your age is:", age)

#Task 33:
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds in your account.")
    return balance - amount

print("Balance after withdrawal:", withdraw(1000, 500))  # ✅
# withdraw(500, 800)  # ❌

#Task 34:
class GradeOutOfRangeError(Exception):
    pass

def assign_grade(marks):
    if marks < 0 or marks > 100:
        raise GradeOutOfRangeError("Marks must be between 0 and 100.")
    return "Pass" if marks >= 40 else "Fail"

print(assign_grade(85))  # ✅
# print(assign_grade(120))  # ❌

#Task 35:
class UnauthorizedAccessError(Exception):
    pass

def access_dashboard(role):
    if role != "admin":
        raise UnauthorizedAccessError("Only admin can access the dashboard.")
    print("Welcome to the dashboard.")

# access_dashboard("user")  # ❌
access_dashboard("admin")  # ✅

#Task 36:
class InvalidFileFormatError(Exception):
    pass

def upload_file(filename):
    if not filename.endswith(".csv"):
        raise InvalidFileFormatError("Only .csv files are allowed.")
    print("File uploaded:", filename)

# upload_file("data.txt")  # ❌
upload_file("data.csv")  # ✅

#Task 37:
class LoginAttemptsExceeded(Exception):
    pass

def login_system():
    correct_password = "pass123"
    attempts = 0
    while attempts < 3:
        pwd = input("Enter password: ")
        if pwd == correct_password:
            print("Login successful.")
            return
        attempts += 1
        print("Wrong password.")
    raise LoginAttemptsExceeded("Too many failed login attempts.")

# login_system()  # Try wrong password 3 times to raise error

#Task 38:
class AlreadyStartedError(Exception):
    pass

class Engine:
    def __init__(self):
        self.started = False

    def start(self):
        if self.started:
            raise AlreadyStartedError("Engine already started.")
        self.started = True
        print("Engine started.")

e = Engine()
e.start()
# e.start()  # ❌ Will raise AlreadyStartedError

#Task 39:
class FileTooLargeError(Exception):
    pass

def validate_file_size(size_in_mb):
    if size_in_mb > 5:
        raise FileTooLargeError("File size exceeds 5MB limit.")
    print("File size is acceptable.")

validate_file_size(3)  # ✅
# validate_file_size(10)  # ❌

#Task 40:
class BelowAbsoluteZeroError(Exception):
    pass

def celsius_to_kelvin(temp_c):
    if temp_c < -273.15:
        raise BelowAbsoluteZeroError("Temperature below absolute zero.")
    return temp_c + 273.15

print("Kelvin:", celsius_to_kelvin(0))       # ✅
# print(celsius_to_kelvin(-300))  # ❌


##Exception Handling in Loops and Functions (41–45)
#Task 41:
valid_numbers = []

while len(valid_numbers) < 5:
    try:
        num = int(input(f"Enter integer {len(valid_numbers)+1}: "))
        valid_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Valid integers:", valid_numbers)

#Task 42:
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return None

# Example usage:
content = read_file("myfile.txt")
if content:
    print(content)

#Task 43:
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except (ValueError, RecursionError) as e:
        print("Error:", e)
        return None

# Example usage:
print(factorial(5))  # ✅
print(factorial(-2)) # ❌

#Task 44:
numbers = []

for i in range(5):
    user_input = input(f"Enter number {i+1}: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print(f"Skipping invalid input: {user_input}")

print("Valid numbers:", numbers)

#Task 45:
inputs = ["10", "abc", "20", "!", "30"]

# Convert valid numbers only
valid_ints = [int(x) for x in inputs if x.isdigit()]
print("Valid using .isdigit():", valid_ints)

# Alternatively, with try-except inside a comprehension:
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return None

filtered = [safe_int(x) for x in inputs]
cleaned = [x for x in filtered if x is not None]
print("Valid using try-except:", cleaned)


##Real-Life Use Case Tasks (46–50)
#Task 46:
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator.")

        print("Result:", result)
    except ValueError as ve:
        print("Value Error:", ve)
    except ZeroDivisionError as ze:
        print("Math Error:", ze)
    except Exception as e:
        print("Unexpected error:", e)


#Task 47:
import shutil
import os

def file_copy_tool():
    try:
        src = input("Enter source file path: ")
        dest = input("Enter destination file path: ")

        if not os.path.exists(src):
            raise FileNotFoundError("Source file does not exist.")
        if not os.path.isfile(src):
            raise Exception("Source is not a file.")

        shutil.copy(src, dest)
        print("File copied successfully.")
    except PermissionError:
        print("Permission denied.")
    except FileNotFoundError as fnf:
        print("Error:", fnf)
    except Exception as e:
        print("Copy failed:", e)


#Task 48:
class ValidationError(Exception):
    pass

def register_user():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        if not username or not password or not age or not email:
            raise ValidationError("All fields are required.")

        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters.")

        if not age.isdigit() or int(age) < 0:
            raise ValidationError("Age must be a positive integer.")

        if "@" not in email or "." not in email:
            raise ValidationError("Invalid email format.")

        print("User registered successfully!")
    except ValidationError as ve:
        print("Registration error:", ve)



#Task 49:
import logging

logging.basicConfig(filename="app_errors.log", level=logging.ERROR)

def log_demo():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        print("Result:", x / y)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("An error occurred. Check 'app_errors.log' for details.")



#Task 50:
class PaymentError(Exception):
    pass

def process_payment():
    try:
        card_number = input("Enter 16-digit card number: ")
        amount = input("Enter payment amount: ")

        if len(card_number) != 16 or not card_number.isdigit():
            raise PaymentError("Invalid card number.")

        amount = float(amount)
        if amount <= 0:
            raise PaymentError("Amount must be greater than 0.")

        # Simulate server issue
        import random
        if random.choice([True, False]):
            raise ConnectionError("Payment server unreachable.")

        print(f"Payment of ₹{amount:.2f} processed successfully.")
    except PaymentError as pe:
        print("Payment failed:", pe)
    except ConnectionError as ce:
        print("Network error:", ce)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print("Unexpected error:", e)

