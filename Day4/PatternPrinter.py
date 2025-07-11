# Pattern Printer App

# Input: Get number of rows from user
rows = int(input("Enter number of rows: "))

# Use nested loops to print the pattern
for i in range(1, rows + 1):       # Outer loop for rows
    for j in range(i):             # Inner loop for stars
        print("*", end=" ")        # Print star on the same line
    print()                        # Move to next line after each row
