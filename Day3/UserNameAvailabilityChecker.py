taken_usernames = ["admin", "john123", "alice", "testuser", "vijay"]
new_username = input("Enter a username to check availability: ").strip().lower()
if new_username in taken_usernames:
    print(f"❌ The username '{new_username}' is already taken. Please try another.")
else:
    print(f"✅ The username '{new_username}' is available!")
