# Ask for user input
name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
job = input("Enter your job title: ").strip()

# Capitalize name
name_upper = name.upper()

# Create the bio using f-string
bio = f"Hi, I'm {name_upper}. I'm {age} years old and I work as a {job}"

# Print the bio
print("\nGenerated Bio:")
print(bio)

# Count total characters in the bio
bio_length = len(bio)
print("\nTotal characters in the bio:", bio_length)
