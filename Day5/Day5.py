##Basic While Loop Tasks (1–10)
# Task 1: Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print("\n")

# Task 2: Print even numbers from 2 to 20 using a while loop.
i = 2
while i <= 20:
    print(i, end=' ')
    i += 2
print("\n")

# Task 3: Print the reverse numbers from 10 to 1.
i = 10
while i >= 1:
    print(i, end=' ')
    i -= 1
print("\n")

# Task 4: Ask the user to enter a number and print all numbers up to that number.
num = int(input("Enter a number: "))
i = 1
while i <= num:
    print(i, end=' ')
    i += 1
print("\n")

# Task 5: Calculate the sum of numbers from 1 to 50 using while.
i = 1
total = 0
while i <= 50:
    total += i
    i += 1
print("Sum from 1 to 50:", total)
print()

# Task 6: Find the factorial of a number using a while loop.
n = int(input("Enter a number to find its factorial: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} is {fact}")
print()

# Task 7: Print all multiples of 3 between 1 and 30.
i = 3
while i <= 30:
    print(i, end=' ')
    i += 3
print("\n")

# Task 8: Take user input until they type "stop".
while True:
    user_input = input("Type something (or type 'stop' to end): ")
    if user_input.lower() == "stop":
        break
    print(f"You typed: {user_input}")
print()

# Task 9: Count from 100 down to 50 in steps of 5.
i = 100
while i >= 50:
    print(i, end=' ')
    i -= 5
print("\n")

# Task 10: Take 5 inputs from user and store them in a list using a while loop.
inputs = []
i = 0
while i < 5:
    val = input(f"Enter value {i+1}: ")
    inputs.append(val)
    i += 1
print("You entered:", inputs)

##Infinite While Loop Tasks (11–15)
#Task 11: Create while True
while True:
    print("Welcome!")





