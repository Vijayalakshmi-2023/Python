# Student Score Analyzer

# Step 1: Collect 5 student marks using a for loop
marks = []
for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

# Step 2: Find maximum, minimum, and sum using loops
max_mark = marks[0]
min_mark = marks[0]
total = 0

for mark in marks:
    # Find maximum
    if mark > max_mark:
        max_mark = mark
    # Find minimum
    if mark < min_mark:
        min_mark = mark
    # Add to total
    total += mark

# Step 3: Calculate average
average = total / len(marks)

# Step 4: Display the results
print(f"\nHighest mark: {max_mark}")
print(f"Lowest mark: {min_mark}")
print(f"Average mark: {average:.2f}")
