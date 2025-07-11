# Custom Multiplication Table Generator

# Input: Get any number from the user
num = int(input("Enter a number: "))

# Generate multiplication table using range(1, 11)
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
