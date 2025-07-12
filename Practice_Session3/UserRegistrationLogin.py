# User Registration & Login System

# Global user list
users = []

# Register a new user
def register():
    print("\n=== User Registration ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Check if username already exists
    for user in users:
        if user['username'] == username:
            print("Username already taken.\n")
            return
    
    # Add user to list
    users.append({'username': username, 'password': password})
    print("User registered successfully!\n")

# Login function with 3 attempts
def login():
    print("\n=== Login ===")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        for user in users:
            if user['username'] == username and user['password'] == password:
                print("Login successful!\n")
                return True

        attempts += 1
        print(f"Invalid credentials. Attempts left: {max_attempts - attempts}\n")
    
    print("Too many failed attempts. Access denied.\n")
    return False

# Show all users (for demo purposes only)
def show_users():
    print("\n=== Registered Users ===")
    if not users:
        print("No users registered.\n")
    else:
        for i, user in enumerate(users, start=1):
            print(f"{i}. Username: {user['username']}")
        print()

# Main menu loop
def main():
    while True:
        print("=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Show Users")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_users()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

# Run the main menu
main()
