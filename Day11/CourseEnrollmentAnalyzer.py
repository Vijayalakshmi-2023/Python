# Course Enrollment Analyzer

# Students enrolled in Python and Java courses
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "Eve", "Frank", "Bob"}

# Students enrolled in both courses (intersection)
both_courses = python_students.intersection(java_students)
print("Students in both Python and Java courses:", both_courses)

# Students exclusive to Python course (difference)
exclusive_python = python_students.difference(java_students)
print("Students only in Python course:", exclusive_python)

# All students enrolled in either course (union)
all_students = python_students.union(java_students)
print("All students in Python or Java courses:", all_students)

# Students in only one of the courses (symmetric difference)
exclusive_students = python_students.symmetric_difference(java_students)
print("Students in only one course:", exclusive_students)
