stored_username = "admin"
stored_password = "12345"
username = input("Enter username: ")
password = input("Enter password: ")
if username is stored_username and password is stored_password:
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")
