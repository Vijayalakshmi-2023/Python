# Input details
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
role = input("Enter your professional role: ").strip()

# Convert each part to uppercase
first = first_name.upper()
last = last_name.upper()
job = role.upper()

# Use .join() to combine with separator
resume_title = " | ".join([first, last, job])

# Display the resume title
print("\nGenerated Resume Title:")
print(resume_title)
