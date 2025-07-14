##🔹 1. Tuple Basics
#Task 1:Create an empty tuple and print its type.
empty_tuple = ()
print(empty_tuple)         # Output: ()
print(type(empty_tuple))   # Output: <class 'tuple'>


#Task 2:Create a tuple with integers, strings, and a float and print each item.
mixed_tuple = (10, "hello", 3.14)
for item in mixed_tuple:
    print(item)


#Task 3:Create a tuple with only one element and print its type.
single_item_tuple = (42,)     # Note the comma!
print(single_item_tuple)      # Output: (42,)
print(type(single_item_tuple))  # Output: <class 'tuple'>
 

#Task 4:Convert a list of numbers [1, 2, 3, 4, 5] to a tuple.
num_list = [1, 2, 3, 4, 5]
num_tuple = tuple(num_list)
print(num_tuple)  # Output: (1, 2, 3, 4, 5)


#Task 5:Convert the string "Python" into a tuple of characters.
text = "Python"
char_tuple = tuple(text)
print(char_tuple)  # Output: ('P', 'y', 't', 'h', 'o', 'n')

##2. Tuple Indexing and Slicing
#Task 6:Access the first and last elements of a tuple.
my_tuple=("Anu","Banu","Charu")
print(my_tuple[0])
print(my_tuple[-1])


#Task 7:Slice a tuple to get the middle 3 elements.
def get_middle_three(t):
    mid = len(t) // 2
    return t[mid-1 : mid+2]
t = (10, 20, 30, 40, 50, 60, 70)
print(get_middle_three(t))  # Output: (30, 40, 50)


#Task 8:Reverse a tuple using slicing.
t = (10, 20, 30, 40, 50)
reversed_t = t[::-1]
print(reversed_t)  # Output: (50, 40, 30, 20, 10)


#Task 9:Access every second element from a tuple using slicing.
t = (10, 20, 30, 40, 50, 60)
every_second = t[::2]
print(every_second)  # Output: (10, 30, 50)


#Task 10:Get a sub-tuple using negative indexing and slicing.
t = (10, 20, 30, 40, 50, 60, 70)
sub = t[-3:]  
print(sub)  # Output: (50, 60, 70)


##🔹 3. Tuple Immutability
#Task 11:Attempt to change a tuple element and handle the resulting error.
t = (10, 20, 30)
try:
    t[1] = 99  # Attempt to change the second element
except TypeError as e:
    print("Error:", e)


#Task 12:Show how to replace a value in a tuple by converting it to a list and back.
t = (10, 20, 30)

# Convert tuple to list
temp_list = list(t)

# Modify the list
temp_list[1] = 99

# Convert back to tuple
new_tuple = tuple(temp_list)

print(new_tuple)  # Output: (10, 99, 30)



#Task 13:Add a new value to a tuple (simulate by tuple concatenation).
my_tuple=(10,20,30)
new_tuple=my_tuple+(40,)
print(new_tuple)

#Task 14:Remove an item from a tuple (simulate by list conversion).
my_tuple=(10,20,30)
temp_list=list(my_tuple)
temp_list.remove(20)
new_tuple=tuple(temp_list)
print(new_tuple)

#Task 15:Demonstrate that tuples cannot be deleted partially (e.g., del tuple[0]).
t = (10, 20, 30)

try:
    del t[0]  # Attempt to delete the first element
except TypeError as e:
    print("Error:", e)

##🔹 4. Tuple Operations
#Task 16:Concatenate two tuples.
tuple1=(1,2,3)
tuple2=(4,5,6)
result=tuple1+tuple2
print(result)


#Task 17:Repeat a tuple 3 times using the * operator.
tuple1=(1,2,3)
repeated=tuple1*3
print(repeated)


#Task 18:Check if an item exists in a tuple using in.
tuple1 = (10, 20, 30, 40)
print(20 in tuple1)  # Output: True
print(50 in tuple1)  # Output: False


#Task 19:Find the length of a tuple using len().
tuple1=(10,20,30,40,50)
print(len(tuple1))


#Task 20:Count the number of times an element occurs in a tuple.
tuple1=(10,20,30,40,50,10,20,10,30,20)
print(tuple1.count(30))


##🔹 5. Tuple Functions and Methods
#Task 21:Use the count() method to count element occurrences.
tuple1=(10,20,30,40,50,10,20,10,30,20)
print(tuple1.count(20))


#Task 22:Use the index() method to find the position of an item.
tuple1=(10,20,30,40,50,10,20,10,30,20)
print(tuple1.index(40))


#Task 23:Use max() and min() on a tuple of numbers.
tuple1=(10,20,30,40,50,10,20,10,30,20)
print(max(tuple1))
print(max(tuple1))


#Task 24:Use sum() to find the total of tuple items.
tuple1=(10,20,30,40,50,10,20,10,30,20)
print(sum(tuple1))


#Task 25:Sort a tuple using sorted() (returns a list).
tuple1=(60,80,10,20,50,30)
sorted_tuple=sorted(tuple1)
print(sorted_tuple)

##🔹 6. Iteration and Looping with Tuples
#Task 26:Iterate over a tuple using a for loop and print all elements.
tuple1 = (10, 20, 30, 40)
for item in tuple1:
    print(item)

#Task 27:Iterate with enumerate() to print index and value.
tuple1= (10, 20, 30, 40)
for index, value in enumerate(tuple1):
    print(f"Index {index}: Value {value}")


#Task 28:Use a while loop to iterate through a tuple.
tuple1 = (10, 20, 30, 40)
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1


#Task 29:Print all even numbers from a tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
for num in tuple1:
    if num % 2 == 0:
        print(num)


#Task 30:Count how many strings start with “A” in a tuple of names.
names = ("Alice", "Bob", "Amanda", "Charlie", "Andrew", "Bella")
count = 0
for name in names:
    if name.startswith("A"):
        count += 1
print("Number of names starting with 'A':", count)

##🔹 7. Nested Tuples
#Task 31:Create a tuple of tuples and access inner elements.
inner_tuple=(1,2,3,(4,5,6))
print(inner_tuple[3][1])


#Task 32:Print all sub-tuples from a nested tuple.
nested = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for sub_tuple in nested:
    print(sub_tuple)


#Task 33:Sum all numbers from a tuple of tuples like ((1,2), (3,4)).
data = ((1, 2), (3, 4))
total = 0
for sub in data:
    for num in sub:
        total += num
print("Sum:", total)  # Output: 10

#Task 34:Flatten a nested tuple of integers using a loop.
nested = ((1, 2), (3, 4), (5, 6))
flattened = ()
for sub in nested:
    for item in sub:
        flattened += (item,)  # Concatenate each item as a single-element tuple
print(flattened)  # Output: (1, 2, 3, 4, 5, 6)


#Task 35:Access the second element of the third sub-tuple.
tuple1 = ((1, 2), (3, 4), (5, 6),(7,8))
print(tuple1[2][1])


##🔹 8. Tuple Packing and Unpacking
#Task 36:Pack multiple values into a tuple and print.
my_tuple = (1, 2, 3, "apple", True)
print(my_tuple)


#Task 37:Unpack a tuple into individual variables.
my_tuple = (1, 2, 3, "apple", True)
# Unpacking the tuple into variables
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: apple
print(e)  # Output: True


#Task 38:Use unpacking to swap two variables.
# Initial values
x = 5
y = 10
# Swapping using unpacking
x, y = y, x
print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 5


#Task 39:Use * to unpack remaining values from a tuple.
t = (1, 2, 3, 4, 5)

# Unpacking with * to capture remaining values
a, b, *rest = t
print(a)     # Output: 1
print(b)     # Output: 2
print(rest)  # Output: [3, 4, 5]


#Task 40:Unpack nested tuples into individual values.
nested_tuple = ((1, 2), (3, 4), (5, 6))
# Unpacking the nested tuples
(a1, a2), (b1, b2), (c1, c2) = nested_tuple
print(a1, a2)  # Output: 1 2
print(b1, b2)  # Output: 3 4
print(c1, c2)  # Output: 5 6


##🔹 9. Tuple Use in Functions
#Task 41:Write a function that returns multiple values as a tuple.
def calculate_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b if b != 0 else None  # Handling division by zero
    return sum_result, diff_result, prod_result, div_result
# Calling the function
results = calculate_operations(10, 5)
# Printing the returned tuple
print(results)  # Output: (15, 5, 50, 2.0)
# Unpacking the tuple
sum_val, diff_val, prod_val, div_val = results
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {prod_val}, Division: {div_val}")


#Task 42:Pass a tuple as an argument to a function and print elements.
def print_elements(t):
    for element in t:
        print(element)
# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
# Passing the tuple to the function
print_elements(my_tuple)
 

#Task 43:Write a function to calculate average of numbers using tuple input.
def calculate_average(numbers):
    # Check if the tuple is not empty
    if len(numbers) == 0:
        return "Tuple is empty, cannot calculate average."
    
    # Calculate the sum and length of the tuple
    total_sum = sum(numbers)
    count = len(numbers)
    
    # Calculate the average
    average = total_sum / count
    return average

# Test the function with a tuple of numbers
numbers_tuple = (10, 20, 30, 40, 50)
avg = calculate_average(numbers_tuple)
print("Average:", avg)  # Output: Average: 30.0


#Task 44:Return both min and max from a tuple using a function.
def find_min_max(t):
    # Check if the tuple is empty
    if not t:
        return "Tuple is empty."
    
    # Use built-in functions to find the min and max
    minimum = min(t)
    maximum = max(t)
    
    return minimum, maximum

# Test the function with a tuple of numbers
numbers_tuple = (10, 20, 30, 40, 50)
min_val, max_val = find_min_max(numbers_tuple)
print(f"Min: {min_val}, Max: {max_val}")  # Output: Min: 10, Max: 50
 

#Task 45:Write a function to merge two tuples.
def merge_tuples(t1, t2):
    return t1 + t2
# Test the function
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = merge_tuples(tuple1, tuple2)
print("Merged Tuple:", merged_tuple)  # Output: Merged Tuple: (1, 2, 3, 4, 5, 6)


##🔹 10. Real-Life Tuple Applications
#Task 46:Store coordinates (latitude, longitude) as tuples and display them.
# Storing latitude and longitude as a tuple
coordinates = (40.7128, -74.0060)  # Example: New York City coordinates
# Displaying the coordinates
latitude, longitude = coordinates
print(f"Latitude: {latitude}, Longitude: {longitude}")


#Task 47:Create a phone book with names and numbers stored as tuples in a list.
# List of phone book entries (name, number)
phone_book = [
    ("Alice", "123-456-7890"),
    ("Bob", "987-654-3210"),
    ("Charlie", "555-555-5555")
]
# Printing all entries
for name, number in phone_book:
    print(f"Name: {name}, Phone Number: {number}")


#Task 48:Represent RGB values of an image pixel using a tuple.
# Representing RGB values for a pixel (Red, Green, Blue)
rgb_pixel = (255, 0, 0)  # This represents the color Red
# Display the RGB value
print(f"RGB Color: {rgb_pixel}")

#Task 49:Store exam results (student_name, score) as tuples and print top scorer.
# List of student results (student_name, score)
exam_results = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 88),
    ("David", 95),
    ("Eve", 78)
]
# Finding the top scorer using the max function (based on the score)
top_scorer = max(exam_results, key=lambda x: x[1])
# Displaying the top scorer
print(f"Top Scorer: {top_scorer[0]} with a score of {top_scorer[1]}")


#Task 50:Use a tuple to represent an immutable configuration (host, port, debug_mode).
# Configuration represented as a tuple (host, port, debug_mode)
config = ("localhost", 8080, True)
# Unpack the tuple for easy access
host, port, debug_mode = config
# Display the configuration
print(f"Host: {host}, Port: {port}, Debug Mode: {debug_mode}")


