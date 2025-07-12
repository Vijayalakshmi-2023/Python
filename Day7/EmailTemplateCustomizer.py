# Input
name = input("Enter your name: ").strip()
course = input("Enter your course name: ").strip()
duration = input("Enter the duration in days: ").strip()

# Using f-string directly
email = f"Dear {name}, your {course} course starts in {duration} days."

print("\nCustomized Email:")
print(email)
