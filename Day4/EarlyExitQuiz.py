# Early Exit Quiz

# List of questions and their correct answers
quiz = [
    ("What is the capital of India?", "Delhi"),
    ("What is 5 + 3?", "8"),
    ("What color is the sky on a clear day?", "Blue"),
    ("Which animal is known as the King of the Jungle?", "Lion"),
    ("How many days are there in a week?", "7")
]

# Ask questions one by one
for question, answer in quiz:
    user_input = input(question + " ")
    if user_input.strip().lower() != answer.lower():
        print("Game Over")
        break
else:
    print("Quiz Completed")
