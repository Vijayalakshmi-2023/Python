# Predefined correct credentials
correct_username = "admin"
correct_password = "1234"

# Allow 3 login attempts
for attempt in range(1, 4):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print(f"Invalid credentials. Attempt {attempt} of 3.")
else:
    # If all attempts fail
    print("Account Locked")
