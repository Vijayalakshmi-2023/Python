import logging

# Configure logging
logging.basicConfig(filename="quiz_errors.log", level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidAnswerError(Exception):
    """Raised when user inputs an invalid choice."""
    pass

# Sample quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {"A": "Earth", "B": "Mars", "C": "Venus", "D": "Saturn"},
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": {"A": "10", "B": "11", "C": "12", "D": "13"},
        "answer": "C"
    }
]

def play_quiz():
    score = 0

    for idx, q in enumerate(quiz, 1):
        try:
            print(f"\nQ{idx}: {q['question']}")
            for key, val in q['options'].items():
                print(f"  {key}. {val}")

            user_input = input("Your answer (A/B/C/D): ").strip().upper()

            if user_input not in q["options"]:
                raise InvalidAnswerError("Answer must be one of A, B, C, or D.")

            if user_input == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is {q['answer']}")

        except InvalidAnswerError as iae:
            print(f"⚠️ Invalid input: {iae}")
            logging.error(f"Question {idx}: {iae}")

        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            logging.error(f"Unexpected error at Question {idx}: {e}")

    print("\n🏁 Quiz Completed!")
    print(f"🎯 Your Score: {score}/{len(quiz)}")

# Run the app
if __name__ == "__main__":
    play_quiz()
