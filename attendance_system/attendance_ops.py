# attendance_ops.py

def mark_attendance(attendance, date, present_rolls):
    attendance[date] = set(present_rolls)

def view_attendance_by_date(attendance, students, date):
    present = attendance.get(date, set())
    return [(roll, name) for roll, name in students if roll in present]

def view_attendance_by_student(attendance, student_roll):
    attended_dates = [date for date, present in attendance.items() if student_roll in present]
    return attended_dates

def find_absentees(attendance, students, date):
    all_rolls = {roll for roll, _ in students}
    present = attendance.get(date, set())
    absent_rolls = all_rolls - present
    return [(roll, name) for roll, name in students if roll in absent_rolls]

def generate_report(attendance, students):
    report = {}
    all_dates = attendance.keys()
    for roll, name in students:
        count = sum(1 for date in all_dates if roll in attendance[date])
        report[(roll, name)] = count
    return report
