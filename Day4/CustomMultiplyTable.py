# Custom Size Multiplication Table

# Input: Get table size from the user
size = int(input("Enter table size (e.g., 5 for 5x5): "))

# Generate multiplication table
for i in range(1, size + 1):        # Outer loop for rows
    for j in range(1, size + 1):    # Inner loop for columns
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # New line after each row
