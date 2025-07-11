gradebook = {}

def add_student():
    name = input("Enter student name: ")
    grades_input = input("Enter grades separated by spaces: ")
    try:
        grades = list(map(float, grades_input.strip().split()))
        gradebook[name] = grades
        print(f"Added {name} with grades: {grades}")
    except ValueError:
        print("Invalid input. Please enter numeric grades separated by spaces.")

def view_students():
    if not gradebook:
        print("No students in the gradebook.")
        return
    for name, grades in gradebook.items():
        avg = sum(grades) / len(grades) if grades else 0
        print(f"{name}: Grades: {grades} | Average: {avg:.2f}")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in gradebook:
        del gradebook[name]
        print(f"{name} has been removed from the gradebook.")
    else:
        print(f"{name} not found.")

def main():
    while True:
        print("\nGradebook Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting Gradebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
