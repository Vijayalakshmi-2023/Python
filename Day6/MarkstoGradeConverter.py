def convert_to_grades(marks):
    # Lambda to convert marks to grade
    mark_to_grade = lambda m: (
        'A' if m >= 90 else
        'B' if m >= 75 else
        'C' if m >= 60 else
        'D' if m >= 40 else
        'F'
    )

    # Use map() to apply grading
    grades = list(map(mark_to_grade, marks))
    return grades

# --- Example Usage ---
marks_list = [95, 82, 67, 59, 43, 37]
grades = convert_to_grades(marks_list)

print("📊 Marks:", marks_list)
print("🎓 Grades:", grades)
