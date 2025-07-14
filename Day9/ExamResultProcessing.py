# Sample student exam results, where each result is represented as (student_name, (subject1_score, subject2_score, ...))
exam_results = [
    ("Akash", (85, 90, 78, 92)),
    ("Bharathi", (88, 76, 94, 81)),
    ("Chawan", (70, 80, 65, 90)),
    ("Divya", (95, 93, 98, 88)),
    ("Evangelin", (84, 87, 91, 89)),
]

# 1. Calculate total and average score for each student
def calculate_total_and_average():
    print("Student Exam Results:")
    for student_name, scores in exam_results:
        total_score = sum(scores)  # Calculate total score
        average_score = total_score / len(scores)  # Calculate average score
        print(f"Student: {student_name}, Total Score: {total_score}, Average Score: {average_score:.2f}")
    print("-" * 30)

# 2. Access specific subject score by indexing (e.g., subject 1: index 0, subject 2: index 1, etc.)
def access_specific_subject_score(student_name, subject_index):
    for name, scores in exam_results:
        if name == student_name:
            if 0 <= subject_index < len(scores):
                print(f"{student_name}'s score in subject {subject_index+1} is: {scores[subject_index]}")
            else:
                print(f"Invalid subject index for {student_name}.")
            return
    print(f"Student {student_name} not found.")
    print("-" * 30)

# 3. Ensure immutability of scores and check if the scores have been altered (tuples are immutable)
def check_scores_immutability():
    print("Immutability Check:")
    original_scores = exam_results[0][1]  # Original scores of the first student (Alice)
    
    # Try to alter the tuple (this will raise an error if uncommented)
    # exam_results[0][1][0] = 95  # Uncommenting this line will raise an error
    
    print(f"Original scores of {exam_results[0][0]}: {original_scores}")
    print(f"Scores are immutable, and cannot be altered directly.")
    print("-" * 30)

# Testing the functions
calculate_total_and_average()  # Calculate and display total and average scores
access_specific_subject_score("Alice", 2)  # Access the score for subject 3 (index 2) of Alice
check_scores_immutability()  # Ensure the immutability of the tuple
