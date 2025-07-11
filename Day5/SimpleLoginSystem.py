correct_password = "admin123"

while True:
    password = input("Enter your password: ")

    if password == correct_password:
        pass  # Placeholder for future logging or actions
        print("✅ Login successful!")
        break
    else:
        print("❌ Incorrect password. Try again.")
