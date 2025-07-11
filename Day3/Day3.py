#Arithmetic Operator(Task1-8)
#Task 1
num1=float(input("Enter First Number: "));
num2=float(input("Enter Second Number: "));
print(num1+num2);
print(num1-num2);
print(num1*num2);
print(num1/num2);
 
#Task 2
num3=20;
num4=3;
print(num3//num4);
print(num3%num4);

#Task  3
Num1=2;
Num2=4;
print(Num1**Num2);

#Task 4
Num3=float(input("Enter the First Number: "));
Num4=float(input("Enter the Second Number: "));
print(Num3+Num4);
print(Num3-Num4);
print(Num3*Num4);
print(Num3/Num4);
print(Num3//Num4);
print(Num3%Num4);
print(Num3**Num4);

#Task 5
def shopping_app():
    print("Welcome to the Shopping App!")
    
    item1_price = float(input("Enter the price of item 1: $"))
    item2_price = float(input("Enter the price of item 2: $"))
    item3_price = float(input("Enter the price of item 3: $"))
    
    total_price = item1_price + item2_price + item3_price
    
    print("\n----- Price Summary -----")
    print(f"Item 1: ${item1_price:.2f}")
    print(f"Item 2: ${item2_price:.2f}")
    print(f"Item 3: ${item3_price:.2f}")
    print("-------------------")
    print(f"Total:  ${total_price:.2f}")

shopping_app()

#Task 6
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print("The average marks are:", average)

#Task 7
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#Task 8
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2 if num2 != 0 else 'Undefined (division by zero)'}")
print(f"Modulus: {num1} % {num2} = {num1 % num2 if num2 != 0 else 'Undefined (modulus by zero)'}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2 if num2 != 0 else 'Undefined (floor division by zero)'}")

##Comparison Operators
#Task 9

num1 = float(input("Enter first number (num1): "))
num2 = float(input("Enter second number (num2): "))
print(f"{num1} is equal to {num2} : {num1 == num2}")
print(f"{num1} is not equal to {num2} : {num1 != num2}")
print(f"{num1} is greater than {num2}  : {num1 > num2}")
print(f"{num1} is less than {num2}  : {num1 < num2}")
print(f"{num1} is greater than or equal to {num2} : {num1 >= num2}")
print(f"{num1} is less than or equal to {num2} : {num1 <= num2}")

#Task 10
age=float(input("Enter Your Age: "));
if age>=18:
    print("You are a Major")
else:
    print("You are a Minor")

#Task 11
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(f"{str1} is equal to {str2} : {str1 == str2}")
print(f"{str1} is not equal to {str2} : {str1 != str2}")

#Task 12
score1=float(input("Enter First Exam Score: "));
score2=float(input("Enter Second Exam Score: "));
if score1 > score2:
    print(f"The first score {score1} is higher than the second score {score2}.")
elif score1 < score2:
    print(f"The second score {score2} is higher than the first score {score1}.")
else:
    print("Both scores are equal.")

#Task 13

num = float(input("Enter a number: "))

min = 0
max = 100

if num >= min and num <= max:
    print(f"The number {num} is within the range {min} to {max}.")
else:
    print(f"The number {num} is outside the range {min} to {max}.")

#Task 14
score = float(input("Enter your score: "))
if score > 50:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you did not pass.")

##Logical Operators Tasks
#Task 15
age = int(input("Enter your age: "))

has_id = input("Do you have an ID? (Yes/No): ").strip().lower()

if age > 18 and has_id == "yes":
    print("You are eligible.")
else:
    print("You are not eligible.")

#Task 16
confirmation = input("Do you want to proceed? (yes/y): ").strip().lower()
if confirmation == "yes" or confirmation == "y":
    print("You chose to proceed.")
else:
    print("You chose not to proceed.")

#Task 17
num = int(input("Enter a number: "))
if not (num > 10):
    print(f"The number {num} is not greater than 10.")
else:
    print(f"The number {num} is greater than 10.")

#Task 18
age = int(input("Enter your age: "))
dress_code = input("Enter your dress code (formal/casual): ").strip().lower()
if age >= 21 and dress_code == "formal":
    print("You are allowed entry to the club.")
else:
    print("You are not allowed entry to the club.")

#Task 19
input1 = input("Enter the first boolean value (True/False): ").strip().lower() == 'true'
input2 = input("Enter the second boolean value (True/False): ").strip().lower() == 'true'
print(f"input1 and input2: {input1 and input2}")
print(f"input1 or input2: {input1 or input2}")
print(f"not input1: {not input1}")
print(f"not input2: {not input2}")

#Task 20
score = float(input("Enter your score: "))
attendance = float(input("Enter your attendance percentage: "))
if (score >= 50 and attendance >= 75) or score >= 60:
    print("You pass!")
else:
    print("You fail.")

##Assignment Operators Tasks
#Task 21
var=10
var+=50
print(f"After Addition Assignment var={var}")
var-=5
print(f"After Subtraction Assignment var={var}")
var/=5
print(f"After Division Assignment var={var}")
var*=5
print(f"After Multiplication Assignment var={var}")
var//=5
print(f"After Floor Division Assignment var={var}")
var%=8
print(f"After Modulus Assignment var={var}")

#Task 22
num=25
num+=5
print(num)

#Task 23
side = float(input("Enter the side length of the square: "))
area = side * side
print(f"Area of the square: {area}")

#Task 24
salary = float(input("Enter your salary: "))
tax_rate = 0.20
tax_deduction = salary * tax_rate
salary -= tax_deduction
print(f"Salary after tax deduction: {salary}")

#Task 25
var=10
var+=14
print(f"After Addition Assignment var={var}")
var-=2
print(f"After Subtraction Assignment var={var}")
var/=2
print(f"After Division Assignment var={var}")
var*=5
print(f"After Multiplication Assignment var={var}")
var//=5
print(f"After Floor Division Assignment var={var}")
var%=8
print(f"After Modulus Assignment var={var}")
var**=2
print(f"After Exponentiation Assignment var={var}")

#Task 26
balance = 1000 
print(f"Initial balance: ${balance}")
while True:
    print("\nChoose a transaction:")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        deposit_amount = float(input("Enter the deposit amount: $"))
        balance += deposit_amount  # Update balance using +=
        print(f"Deposited ${deposit_amount}. New balance: ${balance}")
    
    elif choice == "2":
        withdrawal_amount = float(input("Enter the withdrawal amount: $"))
        if withdrawal_amount > balance:
            print("Insufficient balance for withdrawal!")
        else:
            balance -= withdrawal_amount
            print(f"Withdrew ${withdrawal_amount}. New balance: ${balance}")
    
    elif choice == "3":
        print(f"Final balance: ${balance}. Thank you for using the bank!")
        break
    else:
        print("Invalid choice, please try again.")


##Identity Operator Tasks
#Task 27
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
if list1 is list2:
    print("list1 and list2 refer to the same memory location.")
else:
    print("list1 and list2 do not refer to the same memory location.")

#Task 28
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
if list1 is not list2:
    print("list1 and list2 do not refer to the same memory location.")
else:
    print("list1 and list2 refer to the same memory location.")

#Task 29
a = 10
b = 10
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")

#Task 30
list1 = [1, 2, 3, 4]
list2 = list1
list3=[1,2,3,4]
print(f"list1 is list2: {list1 is list2}")
print(f"list2 is not list3: {list2 is not list3}")
print(f"list1 is list3: {list1 is list3}")

##Membership Operators Tasks
#Task 31
my_string = input("Enter a string: ")
letter = input("Enter a letter to check: ")
if letter in my_string:
    print(f"The letter '{letter}' is present in the string.")
else:
    print(f"The letter '{letter}' is NOT present in the string.")

#Task 32
fruit_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
user_fruit = input("Enter a fruit name: ").strip().lower()
if user_fruit in fruit_list:
    print(f"The fruit '{user_fruit}' is in the list!")
else:
    print(f"The fruit '{user_fruit}' is not in the list.")


#Task 33
my_list = [1, 2, 3, 4, 5]
number = 6

if number not in my_list:
    print(f"{number} is not in the list.")
else:
    print(f"{number} is in the list.")


#Task 34
sentence = "Python is a powerful programming language."
word = "powerful"
if word in sentence:
    print(f"The word '{word}' is found in the sentence.")
else:
    print(f"The word '{word}' is not found in the sentence.")

#Task 35
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
if "age" in my_dict:
    print("Key 'age' exists in the dictionary.")
else:
    print("Key 'age' does not exist in the dictionary.")


##Bitwise Operators Tasks
#Task 36
# Input two integers
a = 12  
b = 5   
and_result = a & b    
or_result = a | b    
xor_result = a ^ b  
print("Bitwise AND:", and_result)
print("Bitwise OR:", or_result)
print("Bitwise XOR:", xor_result)

#Task 37
x = 12
result = ~x
print(f"Original number: {x}")
print(f"Binary representation of {x}: {bin(x)}")
print(f"After applying ~: {result}")
print(f"Binary representation of {result}: {bin(result)}")

#Task 38
x = 10
left_shift = x << 2
right_shift = x >> 2
print(f"Original x       = {x} (binary: {bin(x)})")
print(f"x << 2           = {left_shift} (binary: {bin(left_shift)})")
print(f"x >> 2           = {right_shift} (binary: {bin(right_shift)})")

#Task 39
a = 10    
b = 6     
print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))
print("a & b =", a & b, "->", bin(a & b))
print("a | b =", a | b, "->", bin(a | b))
print("a ^ b =", a ^ b, "->", bin(a ^ b))
print("~a =", ~a, "->", bin(~a))
print("a << 2 =", a << 2, "->", bin(a << 2))
print("a >> 2 =", a >> 2, "->", bin(a >> 2))

#Task 40
def toggle_bit(number, bit_position):
    """
    Toggle the bit at 'bit_position' (0-indexed from right).
    """
    mask = 1 << bit_position
    return number ^ mask

def display_binary(label, value, width=8):
    print(f"{label:<15}: {value:<5} ({format(value, f'0{width}b')})")

number = 0b10101010  # 170 in decimal

display_binary("Original", number)

bit_to_toggle = 1
number = toggle_bit(number, bit_to_toggle)
display_binary(f"Toggled bit {bit_to_toggle}", number)

bit_to_toggle = 3
number = toggle_bit(number, bit_to_toggle)
display_binary(f"Toggled bit {bit_to_toggle}", number)

bit_to_toggle = 1
number = toggle_bit(number, bit_to_toggle)
display_binary(f"Toggled bit {bit_to_toggle} again", number)

##Conditional Statements Basics
#Task 41
age=float(input("Enter Your Age: "))
if age>=18:
    print("You are Eligible to Vote.")

#Task 42
age=float(input("Enter Your Age: "))
if age<=18:
    print("You are a Minor.")
else:
    print("You are an Adult")

#Task 43
mark=float(input("Enter Your Mark: "))
if mark>=90:
    print("Your Grade is A.")
elif mark>=80:
    print("Your Grade is B.")
elif mark>=70:
    print("Your Grade is C.")
else:
    print("You are fail.")

#Task 44
temperature = float(input("Enter the temperature: "))

if temperature > 35:
    print("Hot")
elif 25 <= temperature <= 35:
    print("Warm")
else:
    print("Cool")

#Task 45
num=float(input("Enter any number:"))
if num%2==0:
    print("The Entered Number is Even.")
else:
    print("The Entered Number is Odd.")

##Conditional Statements Intermediate
#Task 46
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")

#Task 47
raining = input("Is it raining? (yes/no): ").strip().lower()

if raining == "yes":
    umbrella = input("Do you have an umbrella? (yes/no): ").strip().lower()
    
    if umbrella == "yes":
        print("You can go outside.")
    else:
        print("Better stay inside.")
else:
    print("You can go outside.")

#Task 48
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").strip().lower()

if age >= 18 and nationality == "indian":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Task 49
operation = input("Choose operation (add/sub): ").strip().lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == "add":
    result = num1 + num2
    print("Result:", result)
elif operation == "sub":
    result = num1 - num2
    print("Result:", result)
else:
    print("Invalid operation. Please choose 'add' or 'sub'.")


#Task 50
marks = float(input("Enter exam marks: "))
attendance = float(input("Enter attendance percentage: "))
if marks >= 40 and attendance >= 75:
    print("Passed")
else:
    print("Failed")
