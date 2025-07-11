# Marks to Grade Converter

# Step 1: Input list of marks (example list or user input)
marks = [95, 82, 67, 74, 45, 88]  # Example marks

# Step 2: Convert each mark to grade using for loop and conditions
print("----- Marks to Grades -----")
for mark in marks:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Mark: {mark} → Grade: {grade}")
print("----------------------------")
