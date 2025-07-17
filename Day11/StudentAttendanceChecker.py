# Student Attendance Checker

# Students enrolled in the class
enrolled_students = {"Alice", "Bob", "Charlie", "David", "Eva"}

# Students who are present today
present_students = {"Alice", "David", "Eva"}

# Find absentees using difference()
absentees = enrolled_students.difference(present_students)
print("Absent students:", absentees)

# Latecomers arriving after initial attendance check
latecomers = {"Bob", "Frank"}

# Add latecomers to the present_students set
present_students.add("Bob")        # Add one latecomer
present_students.update(latecomers) # Add multiple latecomers (Bob already added, no duplication)

print("Updated present students:", present_students)

# Recalculate absentees after latecomers
absentees_after_late = enrolled_students.difference(present_students)
print("Absentees after latecomers added:", absentees_after_late)
