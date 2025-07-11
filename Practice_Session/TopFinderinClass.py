# Topper Finder in Class

# Step 1: Dictionary of students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# Step 2: Initialize variables to track topper
topper_name = ""
topper_marks = 0

# Step 3: Use loop to find student with highest marks
for name, marks in student_marks.items():
    if marks > topper_marks:
        topper_name = name
        topper_marks = marks

# Step 4: Print result
print("----- Class Topper -----")
print(f"Topper: {topper_name}")
print(f"Marks : {topper_marks}")
print("-------------------------")
