# List to store student records
students = []

# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to determine grade based on average
def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

# Function to input and process one student's data
def add_student():
    name = input("Enter student name: ").strip()
    try:
        subjects = int(input("Enter number of subjects: "))
        if subjects <= 0:
            print("❌ Number of subjects must be positive.\n")
            return

        marks = []
        for i in range(subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            if mark < 0 or mark > 100:
                print("❌ Marks should be between 0 and 100.")
                return
            marks.append(mark)

        avg = calculate_average(marks)
        grade = calculate_grade(avg)

        student_data = {
            "name": name,
            "marks": marks,
            "average": avg,
            "grade": grade
        }

        students.append(student_data)
        print(f"\n✅ Student '{name}' added with Grade {grade} (Average: {avg:.2f})\n")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.\n")

# Function to display all student records
def show_all_students():
    if not students:
        print("No student data recorded yet.\n")
        return

    print("\n=== Student Records ===")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("-" * 30)
    print()

# Main loop
def main():
    while True:
        print("=== Student Grade Calculator ===")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Run the program
main()
