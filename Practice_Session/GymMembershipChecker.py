# Gym Membership Checker

# Step 1: Define variables
name = "Alice"
age = 22
bmi = 23.5

# Step 2: Check eligibility using if condition
if age > 18 and bmi < 25:
    eligibility = "Eligible for Gym Offers"
else:
    eligibility = "Not Eligible for Gym Offers"

# Step 3: Display formatted output
print("----- Gym Membership Check -----")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"BMI  : {bmi}")
print(f"Status: {eligibility}")
print("--------------------------------")
