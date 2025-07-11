# List of correct answers
correct_answers = ['A', 'C', 'B', 'D', 'A']

# Input user answers
user_answers = []

print("Enter your answers for the quiz (options A, B, C, D):")
for i in range(len(correct_answers)):
    ans = input(f"Question {i+1}: ").strip().upper()
    user_answers.append(ans)

# Count correct responses
score = 0
for i in range(len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        score += 1

# Assign grade based on score
if score == len(correct_answers):
    grade = 'A+'
elif score >= len(correct_answers) * 0.8:
    grade = 'A'
elif score >= len(correct_answers) * 0.6:
    grade = 'B'
elif score >= len(correct_answers) * 0.4:
    grade = 'C'
else:
    grade = 'F'

# Output result
print(f"\nYour score: {score} out of {len(correct_answers)}")
print(f"Your grade: {grade}")
