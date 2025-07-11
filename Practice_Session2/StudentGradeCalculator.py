# Input: Student name and marks
student_name = "Vijayalakshmi"  # You can change the name as needed
marks = [85, 78, 92, 88, 90]  # Marks in 5 subjects

# Calculate total and average using a for loop
total = 0
for mark in marks:
    total += mark

average = total / len(marks)

# Determine grade using if-elif-else
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# Output the result
print(f"Student: {student_name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")
