while True:
    password = input("Enter a password (at least 6 characters): ")
    if len(password) < 6:
        print("Password too short, try again.")
        continue  # Re-prompt if too short
    else:
        break  # Password accepted, exit loop
else:
    # This else won't run because of the break, but including per requirements
    print("Password accepted")

print("✅ Password accepted!")
