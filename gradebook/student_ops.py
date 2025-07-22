# student_ops.py

def add_student(students, roll_no, name):
    student_key = (roll_no, name)
    students.append({'info': student_key, 'grades': {}})
    return student_key

def update_grade(students, roll_no, subject, grade):
    for student in students:
        if student['info'][0] == roll_no:
            student['grades'][subject] = grade
            break

def calculate_average(student):
    grades = student['grades'].values()
    return sum(grades) / len(grades) if grades else 0

def find_top_performers(students):
    top_avg = 0
    top_students = []
    for student in students:
        avg = calculate_average(student)
        if avg > top_avg:
            top_avg = avg
            top_students = [student]
        elif avg == top_avg:
            top_students.append(student)
    return top_students

def list_unique_subjects(students):
    subjects = set()
    for student in students:
        subjects.update(student['grades'].keys())
    return subjects
