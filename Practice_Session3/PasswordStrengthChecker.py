import string

# Function to check password strength
def is_strong_password(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        return False
    if not has_lower:
        print("❌ Password must include a lowercase letter.")
        return False
    if not has_upper:
        print("❌ Password must include an uppercase letter.")
        return False
    if not has_digit:
        print("❌ Password must include a number.")
        return False
    if not has_symbol:
        print("❌ Password must include a special character (e.g. !, @, #).")
        return False

    return True

# Main loop to prompt user
def main():
    print("=== Password Strength Checker ===")
    while True:
        pwd = input("Enter a strong password: ").strip()
        if is_strong_password(pwd):
            print("✅ Password is strong!\n")
            break
        else:
            print("Please try again.\n")

# Run the checker
main()
