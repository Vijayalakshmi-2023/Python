# Grade Level Checker

# Step 1: Input total marks
total_marks = float(input("Enter total marks: "))

# Step 2: Check grade level using if-elif-else
if total_marks == 90:
    grade = "Excellent"
elif 75 <= total_marks < 90:
    grade = "Good"
elif 50 <= total_marks < 75:
    grade = "Average"
else:
    grade = "Poor"

# Step 3: Display result
print("\n----- Grade Level -----")
print(f"Marks : {total_marks}")
print(f"Grade : {grade}")
print("------------------------")
