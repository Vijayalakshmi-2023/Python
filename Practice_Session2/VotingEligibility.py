# Input: Name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check eligibility
if age >= 18:
    print(f"✅ {name}, you are eligible to vote.")
else:
    print(f"❌ {name}, you are not eligible to vote.")
