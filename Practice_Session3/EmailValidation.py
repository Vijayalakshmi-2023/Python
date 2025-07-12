# Function to check if email is valid
def is_valid_email(email):
    email = email.strip()

    # Basic structure checks
    if len(email) < 6:
        print("❌ Email too short.")
        return False
    if "@" not in email or "." not in email:
        print("❌ Email must contain '@' and '.'")
        return False
    
    at_index = email.find("@")
    dot_index = email.rfind(".")

    # Validate positions
    if at_index < 1 or dot_index < at_index + 2 or dot_index == len(email) - 1:
        print("❌ Invalid email format.")
        return False

    # Optional: Check domain parts
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        print("❌ Invalid domain or username.")
        return False

    return True

# Main loop to prompt for valid email
def main():
    print("=== Email Validation Program ===")
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            print(f"✅ Valid email: {email}\n")
            break
        else:
            print("Please try again.\n")

# Run the email validator
main()
