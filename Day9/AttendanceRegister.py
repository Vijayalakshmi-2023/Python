# Sample classroom attendance register as a list of tuples (date, (students in attendance))
attendance_register = [
    ("2023-10-01", ("Anu", "Banu", "Charu", "Deva")),
    ("2023-10-02", ("Anu", "Banu", "Deva")),
    ("2023-10-03", ("Banu", "Charu", "Deva", "Elan")),
    ("2023-10-04", ("Anu", "Charu", "Deva")),
    ("2023-10-05", ("Anu", "Banu", "Charu"))
]

# 1. Access a specific day's attendance using slicing
def get_attendance_for_day(day_index):
    # Using slicing to access a specific day's attendance
    day_record = attendance_register[day_index]
    date, students = day_record
    print(f"Attendance for {date}: {students}")

# 2. Count how many days a specific student was present
def count_student_attendance(student_name):
    # Using .count() to count how many days the student was present
    count = sum(1 for day in attendance_register if student_name in day[1])
    return count

# 3. Tuple unpacking to print attendance reports
def print_attendance_report():
    print("\nAttendance Report:")
    for record in attendance_register:
        date, students = record
        print(f"Date: {date}, Students Present: {', '.join(students)}")

# Testing the functions
print("Accessing Attendance for Day 2 (2023-10-02):")
get_attendance_for_day(1)  # Day 2 is at index 1 (zero-indexed)

# Count how many times Alice was present
alice_attendance_count = count_student_attendance("Alice")
print(f"\nAlice was present on {alice_attendance_count} days.")

# Print the full attendance report
print_attendance_report()
