students = []
count = 0

while count < 10:
    name = input(f"Enter name of student {count + 1}: ").strip()
    if name == "":
        print("Empty name skipped.")
        continue  # Skip empty names without incrementing count
    students.append(name)
    count += 1
else:
    print("Attendance completed!")

print("\nStudents Present:")
for s in students:
    print(s)

