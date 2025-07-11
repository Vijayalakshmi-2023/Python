correct_password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password.")
    attempts += 1
else:
    # Runs only if loop was NOT broken (i.e., password never matched)
    print("Too many attempts!")
