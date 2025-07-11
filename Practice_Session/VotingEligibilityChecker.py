# Voting Eligibility Checker

# Step 1: Input list of ages (example list)
ages = [12, 17, 18, 25, 16, 30]

# Step 2: Check eligibility using for loop and condition
print("----- Voting Eligibility -----")
for age in ages:
    if age >= 18:
        print(f"Age {age}: Eligible to vote")
    else:
        print(f"Age {age}: Not eligible to vote")
print("------------------------------")
