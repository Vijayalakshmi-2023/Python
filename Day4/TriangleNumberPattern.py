# Triangle Number Pattern App

# Input: Get number of rows
rows = int(input("Enter number of rows: "))

# Generate pattern
for i in range(1, rows + 1):       # Outer loop for rows
    for j in range(1, i + 1):      # Inner loop to print numbers 1 to i
        print(j, end=" ")
    print()                        # Move to next line after each row
