# report_gen.py

from student_ops import calculate_average

def generate_report_card(student):
    roll_no, name = student['info']
    grades = student['grades']
    report = f"\nReport Card for {name} (Roll No: {roll_no})\n"
    report += "-" * 40 + "\n"
    for subject, grade in grades.items():
        report += f"{subject:<15}: {grade}\n"
    avg = calculate_average(student)
    report += "-" * 40 + "\n"
    report += f"Average Grade      : {avg:.2f}\n"
    return report
