##📘 Basic Function Definition and Calling (1–10)
#Task 1: Define a function greet() that prints “Welcome to Python!”.
def greet():
    print("Welcome to Python")
greet()

#Task 2: Write a function add(a, b) that returns the sum of two numbers.
def sum(a,b):
    return (a+b)
result=sum(5,10)
print(result)

#Task 3: Define a function is_even(num) that returns True if the number is even.
def is_even(num):
    return num % 2 == 0
result=is_even(5)
print(result)

#Task 4: Create a function cube(n) that returns the cube of a number.
def cubic(num):
    return num*num*num
result=cubic(3)
print(result)

#Task 5: Write a function hello(name) that prints "Hello, <name>".
def hello(name):
    return(f"Hello, {name}")
result=hello("Anu")
print(result)

#Task 6: Define a function with no code yet using pass.
def function():
    pass #pass is a placeholder that tells Python "do nothing here (for now)."

#Task 7: Create a function that takes two numbers and prints which is greater using if.
def large_number(num1,num2):
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    elif num2>num1:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num1} and {num2} is equal.")
result=large_number(10,8)

#Task 8: Write a function square_area(side) to return the area of a square.
def square_area(side):
    return side*side
result=square_area(4)
print(result)

#Task 9: Create a menu-based function with options (view, add, exit) using if-else.
def menu():
    items = ["Pizza","Burger"]  # List to store items
    
    while True:
        print("\nMenu:")
        print("1. View Items")
        print("2. Add Item")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            if items:
                print("Items:")
                for item in items:
                    print(f"- {item}")
            else:
                print("No items to display.")
        elif choice == '2':
            new_item = input("Enter item to add: ")
            items.append(new_item)
            print(f"'{new_item}' added.")
        elif choice == '3':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
menu()

#Task 10: Call a function multiple times in a loop to show reusability.
def greet(name):
    print(f"Hello, {name}!")

# List of names
names = ["Anu", "Banu", "Charu", "Divya"]

# Call the function for each name in the list
for person in names:
    greet(person)

##📘 Functions with Parameters and Return Values (11–15)
#Task 11: Divide and handle divide-by-zero
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

#Task 12: Return full name
def full_name(fname, lname):
    return (f"Hi,{fname} {lname}")
result=full_name("Vijayalakshmi", "N")
print(result)

#Task 13: Check voting eligibility
def is_eligible_to_vote(age):
    return age >= 18
result=is_eligible_to_vote(14)
print(result)

#Task 14: Calculate discount price
def calc_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price
result=calc_discount(1000,5)
print(result)

#Task 15: Calculate average of 3 numbers
def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3) / 3
result=average_of_three(3,7,11)
print(result)

##📘 Global vs Local Variables (16–20)
#Task 16: Create a global variable x = 100, and print it inside a function.
x = 100
def print_global_x():
    print("The value of global x is:", x)
print_global_x()

#Task 17: Create a function with a local variable and show that it's not accessible outside.
def local_variable_example():
    y = 50
    print("Inside the function, y =", y)
local_variable_example()
print("Outside the function, y =", y)

#Task 18: Use both a global and a local variable in the same function and print both.
# Global variable
x = 100
def global_and_local():
    y = 50  # Local variable
    print("Global variable x =", x)
    print("Local variable y =", y)
global_and_local()

#Task 19: Modify a global variable inside a function using the global keyword.
count = 0
def increment_count():
    global count 
    count += 1
    print("Inside function, count =", count)
increment_count()
increment_count()
print("Outside function, count =", count)

#Task 20: Show that a variable with the same name inside a function doesn’t affect the global one.
message = "Hello from global scope!"
def show_local_message():
    message = "Hello from local scope!"  
    print("Inside function:", message)
show_local_message()
print("Outside function:", message)

##📘 Recursion Tasks (21–25)
#Task 21: Write a recursive function to calculate factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
print(factorial(5)) 

#Task 22: Create a recursive function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
print(fibonacci(6))  

#Task 23: Use recursion to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return s 
    else:
        return reverse_string(s[1:]) + s[0]  
print(reverse_string("hello"))  

#Task 24: Use recursion to sum all elements in a list.
def sum_list(numbers):
    if len(numbers) == 0:
        return 0  
    else:
        return numbers[0] + sum_list(numbers[1:])  
print(sum_list([1, 2, 3, 4, 5]))  

#Task 25: Write a recursive function that counts down from a number to 1.
def countdown(n):
    if n < 1:
        return  
    else:
        print(n)
        countdown(n - 1)  
countdown(5)

##📘 *args and **kwargs Tasks (26–30)
#Task 26: Write a function add_numbers(*args) that returns the sum of all arguments.
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3))        
print(add_numbers(10, 20, 30, 40)) 
print(add_numbers())      

#Task 27: Create a function that prints all positional arguments received via *args.
def print_args(*args):
    for i, arg in enumerate(args, start=1):
        print(f"Argument {i}: {arg}")
print_args("apple", 42, 3.14, True)

#Task 28: Create a function student_info(**kwargs) to print student data.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(name="Alice", age=20, grade="A", major="Physics")

#Task 29: Combine *args and **kwargs in one function and display both.
def display_args_kwargs(*args, **kwargs):
    print("Positional arguments (*args):")
    for i, arg in enumerate(args, start=1):
        print(f"  Arg {i}: {arg}")
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
display_args_kwargs(10, "hello", True, name="Bob", age=25)

#Task 30: Write a function that accepts an unknown number of keyword arguments and filters only those with integer values.
def filter_int_kwargs(**kwargs):
    filtered = {k: v for k, v in kwargs.items() if isinstance(v, int)}
    return filtered
result = filter_int_kwargs(name="Alice", age=20, height=5.5, score=95, active=True)
print(result)  # Output: {'age': 20, 'score': 95}

##📘 Lambda Functions (31–35)
#Task 31: Write a lambda function to add two numbers.
add = lambda a, b: a + b
print(add(5, 3))

#Task 32: Create a lambda to return the square of a number.
square = lambda x: x ** 2
print(square(4)) 
print(square(7)) 

#Task 33: Use lambda with sorted() to sort a list of tuples by second value.
data = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#Task 34: Replace a normal function with a lambda version.
def multiply(a, b):
    return a * b
print(multiply(3, 4))  

multiply = lambda a, b: a * b
print(multiply(3, 4))  

#Task 35: Use a lambda function inside another function (function returning lambda).
def make_power(n):
    return lambda x: x ** n
square = make_power(2)
print(square(5))
cube = make_power(3)
print(cube(3))   

##📘 Built-in Functions: map(), filter(), reduce() (36–40)
#Task 36: Use map() and lambda to square every element in a list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

#Task 37: Use filter() to remove all odd numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#Task 38: Use map() to convert a list of strings to uppercase.
words = ["Hai", "Hello", "Welcome"]
uppercased = list(map(lambda word: word.upper(), words))
print(uppercased) 

#Task 39: Use reduce() to calculate the product of a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  

#Task 40: Use filter() to return words longer than 5 characters from a list.
words = ["apple", "banana", "grapefruit", "kiwi", "orange", "fig"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  

##📘 First-Class Functions (41–45)
#Task 41: Assign a function to a variable and call it using the new name.
def greet(name):
    return f"Hello, {name}!"
say_hello = greet
print(say_hello("Alice")) 

#Task 42: Create a function that takes another function as an argument.
def operate_on_number(func, num):
    return func(num)

# Example function to pass in
def double(x):
    return x * 2
result = operate_on_number(double, 10)
print(result)


#Task 43: Write a function that returns another function.
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
double = make_multiplier(2)
print(double(5))  # Output: 10
triple = make_multiplier(3)
print(triple(4))  # Output: 12


#Task 44: Pass a lambda function as an argument to another function.
def apply_operation(func, value):
    return func(value)
result = apply_operation(lambda x: x ** 2, 6)
print(result) 


#Task 45: Write a function that takes two numbers and a function (like add, subtract) and applies it.
def calculate(num1, num2, operation):
    return operation(num1, num2)
def add(num3, num4):
    return num3+num4
def subtract(num3, num4):
    return num3-num4
print(calculate(10, 5, add))       
print(calculate(10, 5, subtract))  

##📘 Inner Functions (46–47)
#Task 46: Write a function with a nested function inside that prints a message.
def outer_function():
    def inner_function():
        print("Hello from the nested function!")
    inner_function()
outer_function()


#Task 47: Write a function that uses an inner function to double a number, and return the result.
def double_number(num):
    def inner_double(x):
        return x * 2
    return inner_double(num)
result = double_number(5)
print(result)  # Output: 10


##📘 OOP: self and Class-based Function (48–49)
#Task 48: Create a class Person with attributes and a method greet() that uses self.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Anu", 30)
person1.greet()


#Task 49: Create a class Calculator with methods add, subtract, using self.
class Calculator:
    def __init__(self):
        pass  
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
calc = Calculator()
print(calc.add(10, 5))      
print(calc.subtract(10, 5))


##📘 Bonus: Real-World Project-Based Function (50)
#Task 50: Create a billing app with functions:
# Global list to store items as (name, price) tuples
items = []
def add_item(name, price):
    global items
    items.append((name, price))
def get_total():
    global items
    # Extract prices from items
    prices = [price for _, price in items]
    # Use lambda with reduce to sum prices
    total = (lambda *args: sum(args))(*prices)
    return total
def apply_discount(percent):
    global items
    total = get_total()
    discount_amount = total * (percent / 100)
    return total - discount_amount
add_item("Laptop", 15000.0)
add_item("EarBuds", 1299.0)
add_item("Mobile", 10999.0)
print("Total:", get_total()) 
print("Total after 10% discount:", apply_discount(10)) 
