# Format: {question: {"options": [...], "answer": ...}}
quiz_data = {
    "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    "What is the largest ocean on Earth?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
}
# Function to run the quiz
def run_quiz():
    score = 0
    correct_answers = {}
    wrong_answers = {}

    # Loop through the quiz questions
    for question, data in quiz_data.items():
        print(f"\n{question}")
        print("Options: ")
        for i, option in enumerate(data["options"], start=1):
            print(f"{i}. {option}")
        
        # Accept user answer
        user_answer = input("Please select an option (1-4): ")
        
        # Check if the user answer is valid
        if user_answer in ['1', '2', '3', '4']:
            selected_option = data["options"][int(user_answer) - 1]
            if selected_option == data["answer"]:
                score += 1
                correct_answers[question] = selected_option
            else:
                wrong_answers[question] = selected_option
        else:
            print("Invalid option! Please choose a number between 1 and 4.")
    
    # Display the result summary
    print("\nQuiz Result:")
    print(f"Your Score: {score}/{len(quiz_data)}")
    
    # Correct answers summary using comprehension
    print("\nCorrect Answers:")
    for question, answer in correct_answers.items():
        print(f"  {question} -> Correct answer: {answer}")
    
    print("\nWrong Answers:")
    for question, answer in wrong_answers.items():
        print(f"  {question} -> Your answer: {answer}, Correct answer: {quiz_data[question]['answer']}")

    # Final message based on score
    if score == len(quiz_data):
        print("\nPerfect! You scored 100%.")
    elif score > len(quiz_data) // 2:
        print("\nGood job! You passed the quiz.")
    else:
        print("\nBetter luck next time!")
# Run the quiz
run_quiz()
