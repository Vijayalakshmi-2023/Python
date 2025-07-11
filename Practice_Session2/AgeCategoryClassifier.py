# Input: Name and age
name = input("Enter your name: ")

# Validate age input
age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)

    # Classify based on age
    if age < 13:
        category = "Child"
    elif 13 <= age <= 19:
        category = "Teen"
    elif 20 <= age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    # Output message
    print(f"{name}, you are classified as a {category}.")
else:
    print("Invalid age input. Please enter a valid number.")
