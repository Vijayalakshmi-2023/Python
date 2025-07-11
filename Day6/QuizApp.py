def start_quiz():
    def quiz():
        score = 0

        print("🧠 Welcome to the Quiz!\n")

        # Question 1
        ans1 = input("1. What is the capital of France? ").strip().lower()
        if ans1 == "paris":
            score += 1

        # Question 2
        ans2 = input("2. What is 5 + 7? ").strip()
        if ans2 == "12":
            score += 1

        # Question 3
        ans3 = input("3. Which planet is known as the Red Planet? ").strip().lower()
        if ans3 == "mars":
            score += 1

        return score

    total_score = quiz()
    return total_score

# --- Run the Quiz ---
final_score = start_quiz()
print(f"\n✅ You scored: {final_score}/3")
