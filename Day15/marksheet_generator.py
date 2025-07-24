# Custom Exception
class InvalidMarkError(Exception):
    pass

# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 75:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 40:
        return 'C'
    else:
        return 'F'

# Function to process one student
def process_student():
    try:
        name = input("Enter student name: ").strip()
        subjects = ["Math", "Science", "English"]
        marks = []

        for subject in subjects:
            mark = int(input(f"Enter marks for {subject}: "))
            if mark < 0:
                raise ValueError(f"Negative mark entered for {subject}.")
            if mark > 100:
                raise InvalidMarkError(f"Invalid mark (>100) entered for {subject}.")
            marks.append(mark)

    except (ValueError, InvalidMarkError) as e:
        print(f"❌ Error processing student '{name}': {e}")
        return None  # Skip student

    else:
        average = sum(marks) / len(marks)
        grade = calculate_grade(average)
        print(f"\n✅ Marksheet for {name}")
        for i in range(len(subjects)):
            print(f"{subjects[i]}: {marks[i]}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        return name

    finally:
        print("Student processing complete.\n")

# Main loop to handle multiple students
def main():
    num_students = int(input("Enter number of students: "))
    successful = []

    for _ in range(num_students):
        student = process_student()
        if student:
            successful.append(student)

    print("\n🎓 Successfully processed students:")
    for name in successful:
        print("-", name)

# Run the app
main()
