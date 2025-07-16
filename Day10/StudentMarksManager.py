# Initial student data
marks_db = {
    "Anu": {"Math": 90, "Science": 85},
    "Banu": {"Math": 70, "English": 65},
    "Charu": {"Math": 45, "Science": 50, "English": 40}
}

# Add new student or subject
def add_mark(student, subject, mark):
    if student not in marks_db:
        marks_db[student] = {}
    marks_db[student][subject] = mark

# Update mark for existing student/subject
def update_mark(student, subject, new_mark):
    if student in marks_db and subject in marks_db[student]:
        marks_db[student][subject] = new_mark
    else:
        print(f"Cannot update: {student} or subject {subject} not found.")

# Remove a student entirely
def remove_student(student):
    if student in marks_db:
        del marks_db[student]

# Remove a subject for a student
def remove_subject(student, subject):
    if student in marks_db and subject in marks_db[student]:
        del marks_db[student][subject]

# List all students and their average marks
def list_averages():
    print("\nAverage Marks per Student:")
    for student, subjects in marks_db.items():
        total = sum(subjects.values())
        count = len(subjects)
        avg = total / count if count > 0 else 0
        print(f"  {student}: {avg:.2f}")

# Identify the topper (highest total marks)
def find_topper():
    top_student = None
    top_total = -1
    for student, subjects in marks_db.items():
        total = sum(subjects.values())
        if total > top_total:
            top_total = total
            top_student = student
    print(f"\nTopper: {top_student} with {top_total} total marks")

# Get marks safely with .get()
def get_student_mark(student, subject):
    student_data = marks_db.get(student, {})
    return student_data.get(subject, "No data")

# Use dictionary comprehension to find passed students (avg > 50)
def passed_students():
    passed = {
        student: sum(subjects.values()) / len(subjects)
        for student, subjects in marks_db.items()
        if subjects and sum(subjects.values()) / len(subjects) > 50
    }
    print("\nPassed Students (avg > 50):", passed)

# --- Demo Execution ---
add_mark("Diya", "Math", 88)
add_mark("Diya", "Science", 92)
update_mark("Banu", "Math", 75)
remove_subject("Charu", "English")
remove_student("Nonexistent")  # Safe to ignore
print("\nFull Marks DB:", marks_db)
list_averages()
find_topper()
print("\nCharu Science mark (via get):", get_student_mark("Charu", "Science"))
passed_students()
