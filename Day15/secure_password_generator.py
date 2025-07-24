import random
import string
import logging

# Custom Exception
class WeakPasswordCriteriaError(Exception):
    pass

# Setup logging
logging.basicConfig(filename='password_generator.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    try:
        # Assert: password length must be at least 8
        assert length >= 8, "Password must be at least 8 characters long"

        # Build the character pool
        char_pool = ''
        if use_upper:
            char_pool += string.ascii_uppercase
        if use_lower:
            char_pool += string.ascii_lowercase
        if use_digits:
            char_pool += string.digits
        if use_special:
            char_pool += string.punctuation

        # Raise if criteria is too weak
        if not char_pool:
            raise WeakPasswordCriteriaError("At least one character type must be selected")

        # Generate password
        password = ''.join(random.choices(char_pool, k=length))

    except AssertionError as ae:
        print(f"❌ Error: {ae}")
        logging.error(f"Length assertion failed: {ae}")
        return None

    except WeakPasswordCriteriaError as we:
        print(f"❌ Error: {we}")
        logging.error(f"Weak criteria: {we}")
        return None

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        logging.exception("Unexpected exception during password generation")
        return None

    else:
        print(f"✅ Generated Password: {password}")
        return password

    finally:
        print("🔒 Password generation attempt logged.\n")
def get_user_input():
    try:
        length = int(input("Enter password length (min 8): "))
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'

        return length, upper, lower, digits, special

    except ValueError:
        print("❌ Invalid input. Please enter numeric value for length.")
        logging.error("Invalid input: Non-integer length")
        return None
if __name__ == "__main__":
    specs = get_user_input()
    if specs:
        generate_password(*specs)
