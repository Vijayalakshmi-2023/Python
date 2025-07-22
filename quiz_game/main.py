# main.py

from question_bank import questions
from quiz_engine import pick_random_question, ask_question, get_unique_topics

def run_quiz():
    print("=== Welcome to the Quiz Game ===")
    score = 0
    total_questions = min(5, len(questions))  # Ask up to 5 questions
    asked = set()

    for _ in range(total_questions):
        q = pick_random_question(questions, asked)
        correct = ask_question(q)
        if correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n🎯 Final Score: {}/{}".format(score, total_questions))
    print("📚 Topics Covered:", ", ".join(get_unique_topics(questions)))

if __name__ == "__main__":
    run_quiz()
