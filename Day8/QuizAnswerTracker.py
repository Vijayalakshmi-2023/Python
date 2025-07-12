# Correct answers for the quiz (example: 5 questions)
correct_answers = ['A', 'C', 'B', 'D', 'A']
user_answers = []

# Collect user answers
print("📝 Quiz: Please enter your answers (A/B/C/D)")
for i in range(len(correct_answers)):
    answer = input(f"Q{i+1} Answer: ").strip().upper()
    while answer not in ['A', 'B', 'C', 'D']:
        print("❌ Invalid input. Please enter A, B, C, or D.")
        answer = input(f"Q{i+1} Answer: ").strip().upper()
    user_answers.append(answer)

# Evaluate answers
correct = 0
incorrect = 0

print("\n📊 Result Summary:")
for i in range(len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        correct += 1
        print(f"✅ Q{i+1}: Correct")
    else:
        incorrect += 1
        print(f"❌ Q{i+1}: Incorrect (Your answer: {user_answers[i]}, Correct: {correct_answers[i]})")

# Final score
print("\n🎯 Final Score:")
print(f"Total Questions: {len(correct_answers)}")
print(f"Correct Answers: {correct}")
print(f"Incorrect Answers: {incorrect}")
