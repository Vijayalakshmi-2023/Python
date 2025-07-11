# Number Type Classifier

# Input: List of 10 numbers
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Lists to store odd and even numbers
even_numbers = []
odd_numbers = []

# Classify numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Display the results
print("\nEven numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
