##Basic For Loops Task
#Task 1
items=["Pen","Pencil","Eraser"]
for item in items:
    print(item)

#Task 2
name="Vetri"
for char in name:
    print(char)

#Task 3
for num in range(1,11):
    print(num)

#Task 4
for num in range(1,20):
    if num%2!=0:
        print(num)

#Task 5
colors=["Blue","Green","Red","White","Yellow"]
for color in colors:
    print(color)

#Task 6
for num in range(10,0,-1):
    print(num)

#Task 7
n=int(input("Enter a Number: "))
for i in range(1,n+1):
    print(i)

#Task 8
fruits=["Apple","Banana","Cherry"]
for fruit in fruits:
    print(f"I Like {fruit}")

#Task 9
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#Task 10
total = 0
for i in range(1, 51):
    total += i
print("Sum from 1 to 50 is:", total)

##For Loop with Strings
#Task 11
word = "Technology"
vowels = "aeiouAEIOU"

for char in word:
    if char in vowels:
        print(char)

#Task 12
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

#Task 13
text = "Python Loop Practice"
count = 0

for char in text:
    if char.islower():
        count += 1

print(f"Number of lowercase letters: {count}")

#Task 14
text = "Learn Python Fast"
words = text.split()
for word in words:
    print(word)

#Task 15
text = "Python"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print("Reversed string:", reversed_text)

##Range() with For Loops
#Task 16
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

#Task 17
for i in range(2, 21, 2):
    print(i)

#Task 18
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print(f"Numbers from {start} to {end}:")
for i in range(start, end + 1):
    print(i)


#Task 19
print("\nPowers of 2 up to 1024:")
value = 1
while value <= 1024:
    print(value)
    value *= 2


#Task 20
for i in range(1, 11):
    square = i ** 2
    print(f"Square of {i} is {square}")

##Control Statements – break, continue, pass, else
#Task 21
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#Task 22
for i in range(1, 11):
    if i == 5:
        continue 
    print(i)

#Task 23
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(f"Processing number {i}")

#Task 24
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    if num < 0:
        print("Negative number entered. Stopping input.")
        break
    print(f"You entered: {num}")

#Task 25
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

#Task 26
for i in range(1, 4):
    print(i)
else:
    print("Loop complete!")


#Task 27
items = ["Apple", "Banana", "Orange", "Stop", "Grapes", "Mango"]
for item in items:
    if item == "Stop":
        break
    print(item)


#Task 28
text = "VetriTech"
for char in text:
    if char.upper() == "T":
        continue  # Skip letter T (case-insensitive)
    print(char)


#Task 29
for i in range(1, 11):
    if i % 3 == 0:
        pass  # Placeholder for future logic
    else:
        print(i)


#Task 30
for i in range(1, 6):
    print(i)
    if i == 10:  # This condition will never be true
        break
else:
    print("Loop completed without break.")

##Enumerate Function
#Task 31
text = "Python"
for index, char in enumerate(text):
    print(f"{index} - {char}")


#Task 32
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}", end="  ")


#Task 33
text = "Hello World"
for index, char in enumerate(text):
    print(f"{index} - {char}")


#Task 34
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
for roll_no, name in enumerate(students, start=101):
    print(f"Roll No. {roll_no}: {name}")


#Task 35
def print_menu(menu_items):
    for index, item in enumerate(menu_items, start=1):
        print(f"{index}. {item}")
menu = ["Pizza", "Burger", "Pasta", "Salad", "Juice"]
print_menu(menu)

##Nested For Loops
#Task 36
for i in range(1, 4):       
    for j in range(1, 11): 
        print(f"{i} x {j} = {i * j}")
    print() 


#Task 37
# Pattern: Increasing triangle of stars
for i in range(1, 4):          
    for j in range(i):         
        print("*", end=" ")
    print() 

# Print stars in a single line using nested loop
for i in range(1, 4):         
    for j in range(i):         
        print("*", end=" ")


#Task 38
rows = 3  
for i in range(1, rows + 1):       
    for j in range(1, i + 1):    
        print(j, end=" ")
    print()  


#Task 39
list1 = ["Red", "Green", "Blue"]
list2 = ["Circle", "Square", "Triangle"]
for color in list1:
    for shape in list2:
        print(f"{color} - {shape}")


#Task 40
for i in range(1, 6):             
    for j in range(1, 6):        
        print(f"{i * j:2}", end="  ")
    print()  


#Task 41
rows = 3 
for i in range(1, rows + 1):           
    letter = chr(64 + i)                   
    for j in range(i):                     
        print(letter, end=" ")
    print() 


#Task 42
name = input("Enter your name: ")
for i in range(1, len(name) + 1):
    print(name[:i])

#Task 43
title = input("Enter a title: ")
rows = int(input("Enter the number of rows: "))
print(title)
for i in range(2, rows + 2):
    print((str(i) + ' ') * i)


#Task 44
print("shellCopyEdit")
rows = 3
cols = 3
for i in range(rows):
    for j in range(cols):
        print("#", end=" ")
    print()

#Task 45
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()  

##Logic-Based Loop Tasks
#Task 46
num = int(input("Enter a number to find its factorial: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")


#Task 47
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("The maximum number is:", max_num)


#Task 48
original_list = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(original_list) - 1, -1, -1):
    reversed_list.append(original_list[i])
print("Original list:", original_list)
print("Reversed list:", reversed_list)


#Task 49
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Task 50
print("Prime numbers from 1 to 50:")
for num in range(2, 51):
    is_prime = True 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  
    if is_prime:
        print(num, end=" ")