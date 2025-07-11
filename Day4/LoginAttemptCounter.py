# Simple Login Attempt Counter

# Correct credentials
correct_username = "admin"
correct_password = "1234"

# Allow up to 3 attempts
for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check credentials
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect credentials. Try again.\n")
else:
    print("Account Locked")
