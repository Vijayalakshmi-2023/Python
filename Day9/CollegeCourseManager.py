# Sample course data: (course_id, course_name, (credits, faculty))
courses = [
    ("CS101", "Introduction to Computer Science", (3, "Dr. Smith")),
    ("MATH201", "Calculus I", (4, "Dr. Johnson")),
    ("PHYS150", "Physics I", (4, "Dr. Smith")),
    ("ENG110", "English Literature", (3, "Dr. Williams")),
    ("CHEM101", "General Chemistry", (3, "Dr. Johnson")),
    ("BIO205", "Biology", (5, "Dr. Brown"))
]

# 1. Sort courses by credits (ascending order)
def sort_courses_by_credits():
    sorted_courses = sorted(courses, key=lambda x: x[2][0])  # Sort by the number of credits (x[2][0] is the credit value)
    print("Courses sorted by credits:")
    for course in sorted_courses:
        course_id, course_name, (credits, faculty) = course
        print(f"Course: {course_name}, Credits: {credits}, Faculty: {faculty}")
    print("-" * 30)

# 2. Count how many courses a faculty member handles
def count_courses_by_faculty(faculty_name):
    count = sum(1 for course in courses if course[2][1] == faculty_name)  # Count occurrences of faculty_name in the nested tuple
    print(f"{faculty_name} handles {count} course(s).")
    print("-" * 30)

# 3. Display course details using unpacking
def display_courses():
    print("All Courses:")
    for course in courses:
        course_id, course_name, (credits, faculty) = course
        print(f"Course ID: {course_id}, Name: {course_name}, Credits: {credits}, Faculty: {faculty}")
    print("-" * 30)

# Testing the functions
sort_courses_by_credits()  # Sort and display courses by credits
count_courses_by_faculty("Dr. Smith")  # Count how many courses Dr. Smith handles
count_courses_by_faculty("Dr. Johnson")  # Count how many courses Dr. Johnson handles
display_courses()  # Display all courses
