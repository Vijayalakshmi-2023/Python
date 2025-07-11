# Student Attendance System

# Step 1: Input list of student names
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Step 2: Input attendance status and count present students
present_count = 0

print("Enter attendance for each student (P = Present, A = Absent):")
for name in students:
    status = input(f"{name}: ").strip().upper()
    if status == "P":
        present_count += 1

# Step 3: Display attendance summary
print("\n----- Attendance Summary -----")
print(f"Total Students : {len(students)}")
print(f"Present        : {present_count}")
print(f"Absent         : {len(students) - present_count}")
print("--------------------------------")
