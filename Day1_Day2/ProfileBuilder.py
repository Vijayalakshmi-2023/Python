profile = {}

def create_profile():
    print("\nCreate Your Profile")
    profile['name'] = input("Enter your full name: ").strip()
    profile['age'] = input("Enter your age: ").strip()
    profile['email'] = input("Enter your email address: ").strip()
    profile['bio'] = input("Write a short bio about yourself: ").strip()
    print("\nProfile created successfully!")

def view_profile():
    if not profile:
        print("No profile found. Please create one first.")
        return
    print("\nYour Profile:")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")

def edit_profile():
    if not profile:
        print("No profile found. Please create one first.")
        return
    print("\nEdit Profile")
    for key in profile:
        new_val = input(f"Enter new {key} (leave blank to keep current): ").strip()
        if new_val:
            profile[key] = new_val
    print("Profile updated successfully!")

def main():
    while True:
        print("\nProfile Builder Menu")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. Edit Profile")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            create_profile()
        elif choice == '2':
            view_profile()
        elif choice == '3':
            edit_profile()
        elif choice == '4':
            print("Exiting Profile Builder. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
