user_data = {}
count = 0

while count < 5:
    name = input(f"Enter name of user {count + 1}: ").strip()
    
    if name == "":
        print("⚠️ Name cannot be blank. Skipping...")
        continue  # Skip blank names

    age_input = input(f"Enter age of {name}: ")
    
    if not age_input.isdigit():
        print("❌ Invalid age. Please enter a number.")
        continue

    age = int(age_input)

    # Placeholder for future email validation logic
    pass

    user_data[name] = age
    count += 1

# Display collected user info
print("\n✅ Collected User Information:")
for name, age in user_data.items():
    print(f"{name}: {age} years old")
