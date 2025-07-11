# Employee Bonus Report Generator

# List of employees with their performance scores
employees = [
    ("Alice", 92),
    ("Bob", 85),
    ("Charlie", 70),
    ("David", 88),
    ("Eva", 60)
]

# Generate and display bonus report
for name, score in employees:
    if score >= 90:
        bonus = 10000
        grade = "Excellent"
    elif score >= 75:
        bonus = 5000
        grade = "Good"
    else:
        bonus = 2000
        grade = "Needs Improvement"

    print(f"{name}: Score = {score}, Performance = {grade}, Bonus = ₹{bonus}")
