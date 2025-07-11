# Input: Number of rows
rows = int(input("Enter the number of rows: "))

# Generate pattern using nested for loop
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to next line after each row
