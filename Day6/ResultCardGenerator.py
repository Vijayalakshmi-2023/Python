def result_card(**kwargs):
    subjects = kwargs  # subject: marks
    total = sum(subjects.values())
    average = total / len(subjects)

    # Grading logic using lambda and map()
    def grade_mark(m):
        return (
            "A" if m >= 90 else
            "B" if m >= 75 else
            "C" if m >= 60 else
            "D" if m >= 40 else
            "F"
        )

    grades = list(map(grade_mark, subjects.values()))

    # Pass/fail status
    status = "Pass" if all(m >= 40 for m in subjects.values()) else "Fail"

    # Display result
    print("\n📄 Subject-wise Grades:")
    for (subject, mark), grade in zip(subjects.items(), grades):
        print(f"{subject}: {mark} → Grade {grade}")

    return total, round(average, 2), status

# --- Example Usage ---
total, avg, status = result_card(Math=85, Science=92, English=74, History=66, Art=38)

print(f"\n📊 Total Marks: {total}")
print(f"📈 Average: {avg}")
print(f"🎓 Status: {status}")
