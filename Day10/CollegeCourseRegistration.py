# Structure: {student_name: [courses]}
course_registration = {
    "Alice": ["Math", "Physics"],
    "Bob": ["History", "Math"],
    "Charlie": ["Biology", "Chemistry"],
    "David": ["Math", "Chemistry"]
}

# Add a course for a student
def add_course(student_name, course_name):
    if student_name in course_registration:
        if course_name not in course_registration[student_name]:
            course_registration[student_name].append(course_name)
            print(f"{student_name} has been enrolled in {course_name}.")
        else:
            print(f"{student_name} is already enrolled in {course_name}.")
    else:
        print(f"{student_name} is not registered in the system.")

# Drop a course for a student
def drop_course(student_name, course_name):
    if student_name in course_registration:
        if course_name in course_registration[student_name]:
            course_registration[student_name].remove(course_name)
            print(f"{student_name} has dropped {course_name}.")
        else:
            print(f"{student_name} is not enrolled in {course_name}.")
    else:
        print(f"{student_name} is not registered in the system.")

# Show all students enrolled in a specific course
def show_students_in_course(course_name):
    students_in_course = [student for student, courses in course_registration.items() if course_name in courses]
    
    if students_in_course:
        print(f"\nStudents enrolled in {course_name}:")
        for student in students_in_course:
            print(student)
    else:
        print(f"No students are enrolled in {course_name}.")

# Check if a student is enrolled in a course
def is_enrolled(student_name, course_name):
    if student_name in course_registration:
        if course_name in course_registration[student_name]:
            print(f"{student_name} is enrolled in {course_name}.")
        else:
            print(f"{student_name} is not enrolled in {course_name}.")
    else:
        print(f"{student_name} is not registered in the system.")
# Add courses for students
add_course("Alice", "Computer Science")
add_course("Bob", "Math")
add_course("Charlie", "Math")

# Drop a course for a student
drop_course("David", "Math")

# Show students in a specific course
show_students_in_course("Math")

# Check if a student is enrolled in a course
is_enrolled("Alice", "Physics")
is_enrolled("Bob", "Chemistry")
