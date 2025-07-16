# Format: {date: [student_names_present]}
attendance = {
    "2025-07-01": ["Anu", "Banu", "Charu"],
    "2025-07-02": ["Anu", "Diya"],
    "2025-07-03": ["Banu", "Charu", "Diya"],
}
# Add attendance for a specific day
def add_attendance(date, present_students):
    attendance[date] = present_students
    print(f"Attendance for {date} added: {present_students}")

# Mark absentees by checking which students are not present on a specific day
def mark_absentees(date, all_students):
    if date in attendance:
        present_students = attendance[date]
        absentees = [student for student in all_students if student not in present_students]
        print(f"Absentees on {date}: {absentees}")
    else:
        print(f"No attendance record found for {date}.")

# Get all the dates using .keys()
def get_all_dates():
    return list(attendance.keys())

# Reverse query: Get attendance count for a specific student
def get_attendance_count(student_name):
    count = sum(1 for present_students in attendance.values() if student_name in present_students)
    print(f"{student_name} attended {count} days.")

# Add attendance for a specific day
add_attendance("2025-07-04", ["Anu", "Banu"])

# Mark absentees for a specific day
mark_absentees("2025-07-01", ["Anu", "Banu", "Charu", "Diya"])

# Get all dates
print("\nAll attendance dates:", get_all_dates())

# Get attendance count for a specific student
get_attendance_count("Anu")
get_attendance_count("Charu")
