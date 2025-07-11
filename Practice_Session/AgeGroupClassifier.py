# Age Group Classifier

# Step 1: Input age
age = int(input("Enter age: "))

# Step 2: Classify using if-elif-else
if age < 13:
    group = "Child"
elif 13 <= age <= 19:
    group = "Teen"
elif 20 <= age <= 59:
    group = "Adult"
else:
    group = "Senior"

# Step 3: Display result
print("\n----- Age Group -----")
print(f"Age  : {age}")
print(f"Group: {group}")
print("----------------------")
