# Student Report Card Generator

# Step 1: Store student details
student_name = "John Doe"
student_class = "10th Grade"
marks = [85, 78, 92, 88, 76]  # Example subject marks

# Step 2: Calculate total and average using for loop
total_marks = 0
for mark in marks:
    total_marks += mark

average_marks = total_marks / len(marks)

# Step 3: Assign grade using if-elif-else
if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
else:
    grade = 'D'

# Step 4: Print the report using f-string
print("----- Student Report Card -----")
print(f"Name      : {student_name}")
print(f"Class     : {student_class}")
print(f"Marks     : {marks}")
print(f"Total     : {total_marks}")
print(f"Average   : {average_marks:.2f}")
print(f"Grade     : {grade}")
print("--------------------------------")
