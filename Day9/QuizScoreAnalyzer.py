# Sample quiz score data: (user_id, (quiz1_score, quiz2_score, quiz3_score))
quiz_scores = [
    (1, (85, 90, 88)),
    (2, (76, 83, 79)),
    (3, (92, 95, 98)),
    (4, (68, 72, 70)),
]

# 1. Calculate best and worst scores for each user
def calculate_best_worst_scores():
    for user_id, (quiz1, quiz2, quiz3) in quiz_scores:
        best_score = max(quiz1, quiz2, quiz3)
        worst_score = min(quiz1, quiz2, quiz3)
        print(f"User {user_id} - Best Score: {best_score}, Worst Score: {worst_score}")
    print("-" * 30)

# 2. Get the last 2 quiz attempts using tuple slicing
def get_last_two_attempts(user_id):
    for u_id, scores in quiz_scores:
        if u_id == user_id:
            last_two_scores = scores[-2:]  # Slicing the last two quiz attempts
            print(f"User {u_id} - Last 2 quiz attempts: {last_two_scores}")
            break
    print("-" * 30)

# 3. Replace tuple after final submission
def update_final_submission(user_id, new_scores):
    global quiz_scores
    for i, (u_id, _) in enumerate(quiz_scores):
        if u_id == user_id:
            quiz_scores[i] = (u_id, new_scores)  # Replace the user's tuple with new scores
            print(f"User {user_id} final submission updated to: {new_scores}")
            break
    print("-" * 30)

# Testing the functions
calculate_best_worst_scores()  # Calculate best and worst scores for each user

get_last_two_attempts(2)  # Get last 2 attempts of user 2

# Update the final submission for user 4
update_final_submission(4, (80, 85, 90))

# Display updated scores
calculate_best_worst_scores()
