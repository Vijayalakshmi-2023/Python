import requests
import html  # To decode HTML entities (like &quot;)

# Fetch quiz questions from Open Trivia API
def fetch_questions(amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print("Failed to load questions from API.")
        return []

# Ask each question in a loop
def run_quiz(questions):
    score = 0
    index = 0
    total = len(questions)

    while index < total:
        q = questions[index]
        question_text = html.unescape(q['question'])
        correct_answer = html.unescape(q['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in q['incorrect_answers']]

        # Combine and shuffle answers
        options = incorrect_answers + [correct_answer]
        import random
        random.shuffle(options)

        print(f"\nQ{index + 1}: {question_text}")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        try:
            choice = int(input("Your answer (1-4): "))
            if options[choice - 1] == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. Correct answer: {correct_answer}\n")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.\n")

        index += 1

    return score

# Show results
def show_results(score, total):
    percent = (score / total) * 100
    print("=== Quiz Completed ===")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percent:.2f}%\n")

# Main function
def main():
    print("=== Welcome to the Quiz Game (with API) ===")
    questions = fetch_questions(amount=5)

    if questions:
        score = run_quiz(questions)
        show_results(score, len(questions))
    else:
        print("No questions available. Try again later.")

# Run the game
main()
