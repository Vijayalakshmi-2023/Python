# Attendance Report Generator

# Input: List of student names
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Output: Numbered list with "Present" status using enumerate()
for roll_no, name in enumerate(students, start=101):
    print(f"{roll_no}. {name} - Present")
