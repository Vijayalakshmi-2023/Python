# Number Type Analyzer

# Step 1: Input list of numbers (example input)
numbers = [10, -5, 0, 7, -8]

# Step 2: Analyze each number using for loop and if
print("----- Number Analysis -----")
for num in numbers:
    # Check even or odd
    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    # Check positive, negative, or zero
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Print result
    print(f"{num}: {parity}, {sign}")
print("---------------------------")
