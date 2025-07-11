# Dictionary of students and their marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# Initialize variables for tracking topper
topper_name = ""
topper_marks = -1  # Start with a very low number

# Loop through dictionary to find highest marks
for name, marks in students.items():
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

# Output the result
print(f"🎓 Topper: {topper_name} with {topper_marks} marks.")
