
eligible_count = 0
count = 0

while count < 5:
    age_input = input(f"Enter age of person {count + 1}: ").strip()
    
    if not age_input.isdigit():
        print("❌ Invalid age, please enter a number.")
        continue

    age = int(age_input)

    # Placeholder for future address validation
    pass

    if age >= 18:
        print("✅ Eligible to vote.")
        eligible_count += 1
    else:
        print("❌ Not eligible to vote.")

    count += 1

print(f"\nTotal eligible voters: {eligible_count} out of 5")
