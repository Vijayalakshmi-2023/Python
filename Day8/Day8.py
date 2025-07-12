##✅ List Creation & Basic Operations (Tasks 1–10)
#Task 1:Create a list of 5 student names and print it.
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
print("Student List:", students)


#Task 2:Create a list with mixed data types (int, float, string, bool) and display each element.
mixed_list = [42, 3.14, "Python", True]
print("Mixed List Elements:")
for item in mixed_list:
    print(item)


#Task 3:Write a program to accept 5 numbers from the user and store them in a list.
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Entered Numbers:", numbers)
 

#Task 4:Create an empty list and dynamically append 3 user inputs.
data = []
for i in range(3):
    item = input(f"Enter item {i+1}: ")
    data.append(item)
print("Collected Items:", data)


#Task 5:Write a program to create a list of 10 even numbers using a for loop.
even_numbers = []
for i in range(2, 21, 2):  # Even numbers from 2 to 20
    even_numbers.append(i)
print("Even Numbers:", even_numbers)


#Task 6:Create two lists, one with integers and one with strings, then print them together.
int_list = [1, 2, 3]
str_list = ["one", "two", "three"]
print("Integer List:", int_list)
print("String List:", str_list)


#Task 7:Create a list of fruits and print only the first and last items using indexing.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


#Task 8:Use negative indexing to print the second-last item in a list.
colors = ["red", "green", "blue", "yellow"]
print("Second-last color:", colors[-2])


#Task 9:Write a program to count the total number of elements in a list using len().
items = ["pen", "pencil", "notebook", "eraser"]
print("Total items:", len(items))


#Task 10:Check and print the data type of a created list.
my_list = [10, 20, 30]
print("Data type of my_list:", type(my_list))


##✅ Accessing & Indexing Tasks (11–15)
#Task 11:Access and print each element of a list using a for loop with indexing.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("List items using indexing:")
for i in range(len(fruits)):
    print(fruits[i])


#Task 12:Print every alternate item from a list using slicing.
items = ["pen", "pencil", "eraser", "sharpener", "ruler", "marker"]
print("Every alternate item:", items[::2])


#Task 13:Create a list of cities and print the third character of the second city.
cities = ["London", "Paris", "Tokyo", "Berlin"]
print("Third character of second city:", cities[1][2])  # 'r' in 'Paris'


#Task 14:Write a program to reverse a list using slicing.
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


#Task 15:Access the last element of a list using both positive and negative indexing.
colors = ["red", "green", "blue", "yellow"]
# Positive indexing
print("Last element (positive index):", colors[len(colors)-1])
# Negative indexing
print("Last element (negative index):", colors[-1])


##✅ Adding Elements to Lists (Tasks 16–20)
#Task 16:Start with an empty list and use append() to add 5 elements.
my_list = []
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")
my_list.append("date")
my_list.append("elderberry")
print("List after appending 5 elements:", my_list)


#Task 17:Insert an element at the 3rd position in a list.
fruits = ["apple", "banana", "cherry", "date"]
fruits.insert(2, "kiwi")  # Insert at index 2
print("After inserting at 3rd position:", fruits)


#Task 18:Use extend() to add multiple elements to an existing list.
colors = ["red", "green"]
more_colors = ["blue", "yellow", "purple"]
colors.extend(more_colors)
print("After extend():", colors)


#Task 19:Take user input for a name and add it to an existing list of students.
students = ["Alice", "Bob", "Charlie"]
new_student = input("Enter a new student name: ")
students.append(new_student)
print("Updated student list:", students)


#Task 20:Add all elements from one list into another using += and extend().
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Using +=
list1 += list2
print("After += :", list1)
# Reset and use extend()
list1 = [1, 2, 3]
list1.extend(list2)
print("After extend():", list1)

##✅ Updating List Items (Tasks 21–25)
#Task 21:Change the first element of a list to uppercase.
names = ["alice", "bob", "charlie"]
names[0] = names[0].upper()
print("Updated names list:", names)


#Task 22:Modify the price of a product in a list of prices (e.g., change index 2 value to 999).
prices = [100, 250, 450, 600]
prices[2] = 999
print("Updated prices:", prices)


#Task 23:Update all odd numbers in a list by multiplying them by 2.
numbers = [1, 4, 7, 10, 15]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] *= 2
print("Doubled odd numbers:", numbers)


#Task 24:Write a program to replace a fruit in a list with a new fruit.
fruits = ["apple", "banana", "cherry", "date"]
old_fruit = "banana"
new_fruit = "mango"

if old_fruit in fruits:
    index = fruits.index(old_fruit)
    fruits[index] = new_fruit
print("Updated fruits list:", fruits)

#Task 25:Update the value of a nested list item (list[1][2] = 'done').
nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nested[1][2] = 'done'
print("Updated nested list:", nested)

##✅ Removing Elements (Tasks 26–30)
#Task 26:Use remove() to delete a specific value from a list.
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")  # Removes the first occurrence of "banana"
print("After remove():", fruits)


#Task 27:Use pop() without index to remove the last item and print the updated list.
colors = ["red", "green", "blue"]
colors.pop()  # Removes the last item
print("After pop():", colors)


#Task 28:Use pop(index) to remove the 2nd element in a list.
animals = ["dog", "cat", "rabbit", "hamster"]
animals.pop(1)  # Removes element at index 1 ("cat")
print("After pop(1):", animals)


#Task 29:Use del to remove an element at index 3.
numbers = [10, 20, 30, 40, 50]
del numbers[3]  # Removes item at index 3 (40)
print("After del:", numbers)


#Task 30:Use clear() to delete all elements and print the empty list.
items = ["pen", "pencil", "eraser"]
items.clear()  # Empties the list
print("After clear():", items)  # Output: []


##✅ Looping Through Lists (Tasks 31–35)
#Task 31:Iterate through a list and print all elements in uppercase.
fruits = ["apple", "banana", "cherry"]
print("Fruits in uppercase:")
for fruit in fruits:
    print(fruit.upper())


#Task 32:Write a program to find and print all odd numbers in a list.
numbers = [10, 15, 22, 33, 40, 55]
print("Odd numbers in the list:")
for num in numbers:
    if num % 2 != 0:
        print(num)


#Task 33:Print the square of each number in a list using a loop.
nums = [2, 4, 6, 8]
print("Squares of numbers:")
for n in nums:
    print(f"{n}^2 = {n**2}")


#Task 34:Use enumerate() to print the index and value of each item.
colors = ["red", "green", "blue"]
print("Index and color:")
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")


#Task 35:Count how many times the word "apple" appears in a list using a loop.
fruit_list = ["apple", "banana", "apple", "cherry", "apple", "banana"]
count = 0
for fruit in fruit_list:
    if fruit == "apple":
        count += 1
print(f"'apple' appears {count} times.")


##✅ Nested Lists (Tasks 36–40)
#Task 36:Create a nested list for students with name and marks (e.g., ["John", 85]).
students = [
    ["John", 85],
    ["Alice", 92],
    ["Bob", 78]
]


#Task 37:Access and print the name of the 2nd student from the nested list.
print("Second student name:", students[1][0])  # Alice


#Task 38:Update the marks of the first student in a nested list.
students[0][1] = 90  # Changing John's marks from 85 to 90
print("Updated first student:", students[0])


#Task 39:Iterate over a nested list and print all names and marks neatly.
print("All student records:")
for student in students:
    name, marks = student
    print(f"Name: {name}, Marks: {marks}")


#Task 40:Add a new student to the nested list using append().
new_student = ["Diana", 88]
students.append(new_student)
print("\nAfter adding new student:")
for student in students:
    print(f"Name: {student[0]}, Marks: {student[1]}")

##✅ Concatenation, Repetition, Slicing (Tasks 41–45)
#Task 41:Concatenate two lists of numbers and print the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)
 

#Task 42:Repeat a list of strings 3 times using *.
words = ["hello", "world"]
repeated = words * 3
print("Repeated list:", repeated)


#Task 43:Slice a list to get the first 3 elements.
nums = [10, 20, 30, 40, 50]
first_three = nums[:3]
print("First 3 elements:", first_three)


#Task 44:Slice a list to get all elements except the first and last.
data = ["start", "mid1", "mid2", "mid3", "end"]
middle_elements = data[1:-1]
print("Middle elements:", middle_elements)


#Task 45:Merge a list of numbers with a list of strings and display the final list.
numbers = [1, 2, 3]
strings = ["one", "two", "three"]
merged = numbers + strings
print("Merged list:", merged)


##✅ Membership & Conditional Checks (Tasks 46–50)
#Task 46:Ask the user for a fruit name and check if it exists in the list using in.
fruits = ["apple", "banana", "cherry", "date"]
fruit = input("Enter a fruit name: ").lower()
if fruit in fruits:
    print(f"{fruit} is in the list!")
else:
    print(f"{fruit} is NOT in the list.")


#Task 47:Remove an element only if it exists in the list.
items = ["pen", "pencil", "eraser"]
item_to_remove = input("Enter item to remove: ").lower()

if item_to_remove in items:
    items.remove(item_to_remove)
    print(f"{item_to_remove} removed. Updated list:", items)
else:
    print(f"{item_to_remove} not found in list.")


#Task 48:Write a program that counts how many times a specific element appears.
colors = ["red", "blue", "green", "red", "yellow", "red"]
target = input("Enter color to count: ").lower()
count = colors.count(target)
print(f"{target} appears {count} times.")


#Task 49:Check if a number entered by the user exists in a list of marks.
marks = [75, 88, 92, 60, 70]
num = int(input("Enter a mark to search: "))

if num in marks:
    print(f"{num} exists in the list.")
else:
    print(f"{num} does not exist in the list.")


#Task 50:Ask the user for an item and print whether it is present or not in the list.
shopping_list = ["milk", "bread", "eggs", "butter"]
item = input("Enter item to check: ").lower()
print(f"{item} is {'present' if item in shopping_list else 'not present'} in the shopping list.")
