def input_marks(subject_num=1, marks_list=None):
    if marks_list is None:
        marks_list = []
    
    if subject_num > 5:
        return marks_list
  
    try:
        mark = float(input(f"Enter marks for subject {subject_num}: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return input_marks(subject_num, marks_list)
    
    if mark < 0 or mark > 100:
        print("Marks should be between 0 and 100.")
        return input_marks(subject_num, marks_list)
    
    marks_list.append(mark)
    return input_marks(subject_num + 1, marks_list)

def calculate_average_and_grade(marks):
    average = sum(marks) / len(marks)
    
    if average >= 85:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return average, grade

def grading_system():
    marks = input_marks()

    if any(mark < 35 for mark in marks):
        print("One or more subjects have marks below 35. Please re-enter marks.")
        return grading_system()
    
    average, grade = calculate_average_and_grade(marks)
    return average, grade

avg, grd = grading_system()
print(f"Average Marks: {avg:.2f}")
print(f"Grade: {grd}")
