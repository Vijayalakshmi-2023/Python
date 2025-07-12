# Student Score Tracker
students = [['Ram', 85], ['Sam', 78], ['Tina', 92]]

def show_menu():
    print("\n=== Student Score Tracker ===")
    print("1. View all students")
    print("2. Add a student")
    print("3. Remove a student")
    print("4. Update student marks")
    print("5. Find highest scorer")
    print("6. Find lowest scorer")
    print("7. Sort by marks (descending)")
    print("8. Exit")

def view_students():
    if not students:
        print("No students in the list.")
    else:
        print("\nStudent Records:")
        for name, mark in students:
            print(f"{name}: {mark} marks")

def add_student():
    name = input("Enter student name: ").strip()
    mark = int(input("Enter marks: "))
    students.append([name, mark])
    print(f"{name} added with {mark} marks.")

def remove_student():
    name = input("Enter student name to remove: ").strip()
    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            print(f"{name} removed.")
            return
    print(f"{name} not found.")

def update_marks():
    name = input("Enter student name to update: ").strip()
    for student in students:
        if student[0].lower() == name.lower():
            new_mark = int(input("Enter new marks: "))
            student[1] = new_mark
            print(f"{name}'s marks updated to {new_mark}.")
            return
    print(f"{name} not found.")

def highest_scorer():
    if students:
        top = max(students, key=lambda s: s[1])
        print(f"🏆 Highest scorer: {top[0]} with {top[1]} marks")
    else:
        print("No students available.")

def lowest_scorer():
    if students:
        low = min(students, key=lambda s: s[1])
        print(f"📉 Lowest scorer: {low[0]} with {low[1]} marks")
    else:
        print("No students available.")

def sort_by_marks():
    if students:
        sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
        print("\nStudents sorted by marks (high to low):")
        for name, mark in sorted_students:
            print(f"{name}: {mark} marks")
    else:
        print("No students available.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–8): ")

    if choice == '1':
        view_students()
    elif choice == '2':
        add_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        update_marks()
    elif choice == '5':
        highest_scorer()
    elif choice == '6':
        lowest_scorer()
    elif choice == '7':
        sort_by_marks()
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
