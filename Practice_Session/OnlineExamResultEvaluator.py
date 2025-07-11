# Online Exam Result Evaluator

# Step 1: Take 5 subject marks in a list
marks = [65, 70, 58, 80, 90]  # Example marks

# Step 2: Calculate total and percentage using for loop
total = 0
for mark in marks:
    total += mark

percentage = total / len(marks)

# Step 3: Check for pass/fail
if any(mark < 35 for mark in marks):
    result = "Fail"
    division = "No Division"
else:
    result = "Pass"
    # Step 4: Assign division based on percentage
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 50:
        division = "Second Division"
    elif percentage >= 35:
        division = "Third Division"
    else:
        division = "No Division"

# Step 5: Print the result
print("----- Exam Result -----")
print(f"Marks      : {marks}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {result}")
print(f"Division   : {division}")
print("------------------------")
