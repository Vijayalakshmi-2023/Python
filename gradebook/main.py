# main.py

from student_ops import add_student, update_grade, find_top_performers, list_unique_subjects
from report_gen import generate_report_card

# Initialize student list
students = []

# Add students
add_student(students, 101, "Alice")
add_student(students, 102, "Bob")
add_student(students, 103, "Charlie")

# Update grades
update_grade(students, 101, "Math", 85)
update_grade(students, 101, "Science", 92)
update_grade(students, 102, "Math", 88)
update_grade(students, 102, "Science", 76)
update_grade(students, 103, "Math", 92)
update_grade(students, 103, "Science", 88)

# Display report cards
for student in students:
    print(generate_report_card(student))

# Show top performers
print("\nTop Performers:")
top_students = find_top_performers(students)
for student in top_students:
    print(f"{student['info'][1]} (Roll No: {student['info'][0]})")

# List unique subjects
subjects = list_unique_subjects(students)
print("\nUnique Subjects:", ", ".join(subjects))
