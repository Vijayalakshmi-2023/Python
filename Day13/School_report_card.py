class Person:
    def __init__(self, name, id_no):
        self._name = name
        self._id_no = id_no

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id_no

    def __str__(self):
        return f"{self._name} (ID: {self._id_no})"

class Student(Person):
    def __init__(self, name, id_no, grade_level):
        super().__init__(name, id_no)
        self.__grade_level = grade_level
        self.__marks = {}  # subject: score

    def get_grade_level(self):
        return self.__grade_level

    def get_marks(self):
        return self.__marks.copy()

    def update_marks(self, subject, score):
        self.__marks[subject] = score

    def __str__(self):
        return f"Student: {super().__str__()} | Grade: {self.__grade_level}"

class Teacher(Person):
    def __init__(self, name, id_no, subject):
        super().__init__(name, id_no)
        self.subject = subject

    def assign_marks(self, student, score):
        student.update_marks(self.subject.get_name(), score)

    def __str__(self):
        return f"Teacher: {super().__str__()} | Subject: {self.subject.get_name()}"

class Subject:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def calculate_grade(self, score):
        if score >= 90:
            return 'A'
        elif score >= 75:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 40:
            return 'D'
        else:
            return 'F'

class PracticalSubject(Subject):
    def calculate_grade(self, score):
        return "Pass" if score >= 50 else "Fail"

class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate(self, subjects):
        print(f"\n--- Report Card for {self.student.get_name()} ---")
        marks = self.student.get_marks()
        for subj in subjects:
            name = subj.get_name()
            score = marks.get(name, "N/A")
            grade = subj.calculate_grade(score) if isinstance(score, int) else "N/A"
            print(f"{name:15}: {score:>3} → Grade: {grade}")
        print("-" * 35)

# Subjects
math = Subject("Mathematics")
science = Subject("Science")
lab = PracticalSubject("Computer Lab")  # Polymorphism

# Student
s1 = Student("Ananya", "S101", "10th Grade")

# Teachers
t1 = Teacher("Mr. Ravi", "T01", math)
t2 = Teacher("Mrs. Meera", "T02", science)
t3 = Teacher("Ms. Neha", "T03", lab)

# Assign marks
t1.assign_marks(s1, 88)
t2.assign_marks(s1, 76)
t3.assign_marks(s1, 45)

# Generate Report
report = ReportCard(s1)
report.generate([math, science, lab])
