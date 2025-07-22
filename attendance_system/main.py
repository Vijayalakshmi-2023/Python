# main.py

from data_store import students, attendance
from attendance_ops import (
    mark_attendance, view_attendance_by_date,
    view_attendance_by_student, find_absentees, generate_report
)

# Mark sample attendance
mark_attendance(attendance, "2025-07-22", [101, 103])
mark_attendance(attendance, "2025-07-23", [102, 103, 104])

# View attendance by date
print("\n📅 Attendance on 2025-07-22:")
for roll, name in view_attendance_by_date(attendance, students, "2025-07-22"):
    print(f"{roll} - {name}")

# View attendance by student
print("\n👤 Dates attended by Bob (102):")
for date in view_attendance_by_student(attendance, 102):
    print(date)

# View absentees
print("\n❌ Absentees on 2025-07-23:")
for roll, name in find_absentees(attendance, students, "2025-07-23"):
    print(f"{roll} - {name}")

# Attendance report
print("\n📊 Attendance Report:")
report = generate_report(attendance, students)
for (roll, name), days in report.items():
    print(f"{roll} - {name}: Present on {days} day(s)")
