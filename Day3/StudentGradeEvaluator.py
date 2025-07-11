name = input("Enter student name: ")

print("Enter marks for 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

print("\n📘 Student Report")
print("------------------------")
print(f"Name        : {name}")
print(f"Total Marks : {total}/500")
print(f"Average     : {average:.2f}")
print(f"Grade       : {grade}")
