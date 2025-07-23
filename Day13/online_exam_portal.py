from abc import ABC, abstractmethod

# ---------------------
# Abstract User class
# ---------------------
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_profile(self):
        pass

# ---------------------
# Question class
# ---------------------
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.__answer = answer  # private attribute

    def check_answer(self, user_answer):
        return user_answer.lower().strip() == self.__answer.lower().strip()

    def __str__(self):
        option_text = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(self.options)])
        return f"{self.text}\n{option_text}"

# ---------------------
# Exam class
# ---------------------
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def take_exam(self, student):
        print(f"\n--- {self.title} ---")
        score = 0
        for q in self.questions:
            print("\n" + str(q))
            answer = input("Your answer (A/B/C/D): ")
            idx = ord(answer.upper()) - 65
            if 0 <= idx < len(q.options):
                user_choice = q.options[idx]
                if q.check_answer(user_choice):
                    score += 1
        student.update_score(self.title, score, len(self.questions))

# ---------------------
# Admin class
# ---------------------
class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def show_profile(self):
        print(f"Admin: {self.name}")

    def create_exam(self, title):
        return Exam(title)

    def add_question_to_exam(self, exam, text, options, answer):
        q = Question(text, options, answer)
        exam.add_question(q)

# ---------------------
# Student class
# ---------------------
class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.__scores = {}  # private scores dict

    def show_profile(self):
        print(f"Student: {self.name}")

    def update_score(self, exam_title, score, total):
        self.__scores[exam_title] = (score, total)

    def show_results(self):
        print(f"\n--- Results for {self.name} ---")
        for exam, (score, total) in self.__scores.items():
            print(f"{exam}: {score}/{total}")

# Admin adds exam and questions
admin = Admin("Dr. Rao")
exam = admin.create_exam("Python Basics")

admin.add_question_to_exam(exam, "What is output of 2+2?", ["2", "4", "6", "8"], "4")
admin.add_question_to_exam(exam, "What is the keyword to define function?", ["define", "fun", "def", "function"], "def")

# Student appears for exam
student = Student("Anjali")
student.show_profile()
exam.take_exam(student)
student.show_results()
