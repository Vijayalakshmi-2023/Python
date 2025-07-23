# ----------------------------
# Base Class: Person
# ----------------------------
class Person:
    def __init__(self, name, age, email):
        self._name = name              # Encapsulated attributes
        self._age = age
        self._email = email

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, Email: {self._email}"

# ----------------------------
# Aggregated Class: Department
# ----------------------------
class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Department: {self.name} ({self.code})"

# ----------------------------
# Support Class: AdmissionForm
# ----------------------------
class AdmissionForm:
    def __init__(self, marks, documents_submitted):
        self.__marks = marks
        self.__documents_submitted = documents_submitted

    def is_eligible(self):
        return self.__marks >= 60 and self.__documents_submitted

# ----------------------------
# Subclass: Student (inherits Person)
# ----------------------------
class Student(Person):
    def __init__(self, name, age, email, admission_form, department):
        super().__init__(name, age, email)  # Inherit from Person
        self.__admission_form = admission_form
        self.__department = department

    def admit(self):
        if self.__admission_form.is_eligible():
            print(f"Admission Successful for {self._name}")
            print(f"Allocated -> {self.__department}")
        else:
            print(f"Admission Failed for {self._name}: Ineligible")

    def __str__(self):
        return f"{self.get_details()}, Dept: {self.__department.name}"

# Departments
cs_dept = Department("Computer Science", "CSE01")
math_dept = Department("Mathematics", "MAT01")

# Admission forms
form1 = AdmissionForm(marks=85, documents_submitted=True)
form2 = AdmissionForm(marks=45, documents_submitted=True)

# Students
student1 = Student("Ravi", 18, "ravi@example.com", form1, cs_dept)
student2 = Student("Anu", 17, "anu@example.com", form2, math_dept)

# Admit students
student1.admit()
student2.admit()

# Display student data
print("\n--- Student Summary ---")
print(student1)
print(student2)
