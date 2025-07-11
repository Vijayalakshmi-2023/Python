questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    }
]

def run_quiz():
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
