# Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"

# Instructor class
class Instructor:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def __str__(self):
        return f"Instructor: {self.name} | Expertise: {self.expertise}"

# Base Assignment class (polymorphic)
class Assignment:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def submit(self, content):
        raise NotImplementedError("Subclass must override submit()")

    def __str__(self):
        return f"Assignment: {self.title} (Due: {self.due_date})"

# Essay Assignment - overrides submit
class EssayAssignment(Assignment):
    def submit(self, content):
        print(f"📄 Essay submitted: '{content[:30]}...'")

# MCQ Assignment - overrides submit
class MCQAssignment(Assignment):
    def submit(self, selected_options):
        print(f"✅ MCQ submitted: Options - {selected_options}")

# Course class (aggregates student, instructor, assignments)
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.instructor = None
        self.assignments = []

    def enroll_student(self, student):
        self.students.append(student)

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def course_summary(self):
        print(f"\n📚 Course: {self.course_name}")
        print(f"{self.instructor}")
        print("👨‍🎓 Students:")
        for s in self.students:
            print(f" - {s}")
        print("📝 Assignments:")
        for a in self.assignments:
            print(f" - {a}")

# Create course
python_course = Course("Python Programming")

# Add instructor
instructor = Instructor("Dr. Ada Lovelace", "Python & Algorithms")
python_course.assign_instructor(instructor)

# Enroll students
s1 = Student("Alice", "S001")
s2 = Student("Bob", "S002")
python_course.enroll_student(s1)
python_course.enroll_student(s2)

# Create and add assignments
essay = EssayAssignment("OOP Essay", "2025-08-01")
mcq = MCQAssignment("Basics Quiz", "2025-07-30")
python_course.add_assignment(essay)
python_course.add_assignment(mcq)

# Course overview
python_course.course_summary()

# Students submit assignments
print("\n🧾 Submissions:")
essay.submit("Object-Oriented Programming focuses on classes and objects...")
mcq.submit(["A", "C", "D"])
