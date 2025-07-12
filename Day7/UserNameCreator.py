# Input full name
full_name = input("Enter your full name (first and last): ").strip()

# Split into first and last names
first_name, last_name = full_name.split()

# Slice first 3 letters of first name and last 2 letters of last name
username = first_name[:3] + last_name[-2:]

print("\nGenerated username:", username)
