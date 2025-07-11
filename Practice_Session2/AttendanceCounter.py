# List to store attendance for 7 days
attendance = []

# Taking input for 7 days
print("Enter attendance for 7 days (P for Present, A for Absent):")
for i in range(1, 8):
    day = input(f"Day {i}: ").strip().upper()  # Get input and standardize to uppercase
    if day == 'P' or day == 'A':
        attendance.append(day)
    else:
        print("Invalid input. Please enter 'P' or 'A'.")
        day = input(f"Day {i} (again): ").strip().upper()
        attendance.append(day)

# Count total 'P' in the list
total_present = 0
for status in attendance:
    if status == 'P':
        total_present += 1

# Check eligibility
print(f"\nTotal Presents: {total_present}")
if total_present >= 5:
    print("✅ Eligible for exam.")
else:
    print("❌ Not eligible for exam.")
