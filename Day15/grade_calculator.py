valid_grades = []  # Global list to store valid grades

def enter_grade():
    try:
        grade_input = input("Enter grade (0–100) or type 'done' to finish: ").strip()

        if grade_input.lower() == 'done':
            return  # Exit recursion

        grade = float(grade_input)  # May raise ValueError

        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")

        valid_grades.append(grade)  # Store valid grade

    except ValueError as ve:
        print(f"❌ Invalid input: {ve}")
    finally:
        # Always continue unless user typed 'done'
        if grade_input.lower() != 'done':
            enter_grade()

# Main program
if __name__ == "__main__":
    print("🎓 Welcome to Grade Entry (type 'done' to stop)\n")
    enter_grade()

    print("\n📊 Grade Entry Complete")
    print(f"✅ Total valid grades entered: {len(valid_grades)}")
    if valid_grades:
        average = sum(valid_grades) / len(valid_grades)
        print(f"📈 Average Grade: {average:.2f}")
