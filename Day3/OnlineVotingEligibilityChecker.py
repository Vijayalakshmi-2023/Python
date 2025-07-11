# Input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship status: ").strip().lower()

# Display data types
print(f"\nData Types:")
print(f"Name         : {type(name)}")
print(f"Age          : {type(age)}")
print(f"Citizenship  : {type(citizenship)}")

# Check voting eligibility
if age >= 18 and citizenship == "indian":
    print(f"\n{name}, you are eligible to vote.")
else:
    print(f"\n{name}, you are NOT eligible to vote.")
