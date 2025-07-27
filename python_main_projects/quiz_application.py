import time
import random
import json
from datetime import timedelta

# Question bank format:
# { 'difficulty': {'questions': [list_of_questions]}}

class QuizApp:
    def __init__(self):
        self.score = 0
        self.question_bank = {}

    # Load question bank from a JSON file
    def load_question_bank(self, filename="question_bank.json"):
        try:
            with open(filename, "r") as file:
                self.question_bank = json.load(file)
            print(f"Question bank loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found. Please make sure the file exists.")
        except json.JSONDecodeError:
            print(f"Error reading {filename}. Please check the file format.")

    # Save question bank to a JSON file
    def save_question_bank(self, filename="question_bank.json"):
        with open(filename, "w") as file:
            json.dump(self.question_bank, file, indent=4)
        print(f"Question bank saved to {filename}")

    # Add a question to the question bank
    def add_question(self, difficulty, question, choices, correct_answer):
        question_data = {
            "question": question,
            "choices": choices,
            "correct_answer": correct_answer
        }
        if difficulty not in self.question_bank:
            self.question_bank[difficulty] = {"questions": []}
        self.question_bank[difficulty]["questions"].append(question_data)
        print("Question added to the bank!")

    # Ask a multiple choice question
    def ask_mcq(self, question_data):
        print("\n" + question_data["question"])
        for idx, choice in enumerate(question_data["choices"], 1):
            print(f"{idx}. {choice}")
        answer = input("Your answer: ")

        # Check if the answer is correct
        if question_data["choices"][int(answer) - 1] == question_data["correct_answer"]:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was: {question_data['correct_answer']}")

    # Ask a True/False question
    def ask_true_false(self, question_data):
        print("\n" + question_data["question"])
        answer = input("Your answer (True/False): ").strip().capitalize()

        # Check if the answer is correct
        if answer == question_data["correct_answer"]:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was: {question_data['correct_answer']}")

    # Run the quiz with a timer
    def start_quiz(self, difficulty="Easy", time_limit=30):
        if difficulty not in self.question_bank:
            print(f"No questions available for the {difficulty} difficulty level.")
            return

        questions = self.question_bank[difficulty]["questions"]
        random.shuffle(questions)

        # Timer logic
        start_time = time.time()
        end_time = start_time + time_limit

        print(f"\nStarting {difficulty} quiz with a time limit of {time_limit} seconds...")

        for question_data in questions:
            if time.time() > end_time:
                print("\nTime's up!")
                break

            # Ask the question based on its type
            if isinstance(question_data["choices"], list):  # MCQ
                self.ask_mcq(question_data)
            else:  # True/False
                self.ask_true_false(question_data)

        elapsed_time = time.time() - start_time
        remaining_time = max(0, end_time - time.time())

        print(f"\nQuiz finished! Your score: {self.score}")
        print(f"Time taken: {str(timedelta(seconds=int(elapsed_time)))}")
        print(f"Remaining time: {str(timedelta(seconds=int(remaining_time)))}")

    # Show score summary
    def show_score(self):
        print(f"\nYour score: {self.score}")
    
# Sample question bank data format
sample_questions = {
    "Easy": {
        "questions": [
            {
                "question": "What is 2 + 2?",
                "choices": ["3", "4", "5", "6"],
                "correct_answer": "4"
            },
            {
                "question": "Is the sky blue? (True/False)",
                "choices": ["True", "False"],
                "correct_answer": "True"
            }
        ]
    },
    "Medium": {
        "questions": [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Is Python a programming language? (True/False)",
                "choices": ["True", "False"],
                "correct_answer": "True"
            }
        ]
    },
    "Hard": {
        "questions": [
            {
                "question": "Who developed the theory of relativity?",
                "choices": ["Isaac Newton", "Albert Einstein", "Galileo", "Marie Curie"],
                "correct_answer": "Albert Einstein"
            },
            {
                "question": "Is the Earth flat? (True/False)",
                "choices": ["True", "False"],
                "correct_answer": "False"
            }
        ]
    }
}

# Main execution
def main():
    quiz_app = QuizApp()

    # Load a pre-existing question bank or use sample questions
    quiz_app.question_bank = sample_questions  # Replace with `quiz_app.load_question_bank()` to load from a file.

    while True:
        print("\n=== Quiz Application ===")
        print("1. Start Quiz")
        print("2. Add Question to Bank")
        print("3. Show Score")
        print("4. Save Question Bank")
        print("5. Load Question Bank")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            difficulty = input("Choose difficulty (Easy/Medium/Hard): ").capitalize()
            time_limit = int(input("Enter time limit for the quiz (in seconds): "))
            quiz_app.start_quiz(difficulty=difficulty, time_limit=time_limit)

        elif choice == '2':
            difficulty = input("Enter difficulty (Easy/Medium/Hard): ").capitalize()
            question = input("Enter the question: ")
            print("Enter the choices, separated by commas:")
            choices = input().split(",")
            correct_answer = input("Enter the correct answer: ")
            quiz_app.add_question(difficulty, question, choices, correct_answer)

        elif choice == '3':
            quiz_app.show_score()

        elif choice == '4':
            filename = input("Enter the filename to save the question bank: ")
            quiz_app.save_question_bank(filename)

        elif choice == '5':
            filename = input("Enter the filename to load the question bank from: ")
            quiz_app.load_question_bank(filename)

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
