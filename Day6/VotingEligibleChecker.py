def check_voting_eligibility(age):
    is_eligible = lambda a: a >= 18
    if is_eligible(age):
        return "✅ You are eligible to vote."
    else:
        return "❌ You are not eligible to vote."

# --- Example Usage ---
try:
    user_age = int(input("Enter your age: "))
    result = check_voting_eligibility(user_age)
    print(result)
except ValueError:
    print("⚠️ Invalid input. Please enter a valid number.")
