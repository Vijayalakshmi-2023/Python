# Input: List of 10 numbers
numbers = [12, 7, 5, 18, 23, 44, 9, 2, 10, 17]  # You can change or take user input

# Classify each number as even or odd
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
