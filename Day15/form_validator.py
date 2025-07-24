import logging

# Setup logging
logging.basicConfig(filename="registration_errors.log",
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception for password
class PasswordTooWeakError(Exception):
    pass

def validate_registration():
    try:
        # Input
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age_input = input("Enter your age: ")
        password = input("Enter your password: ")

        # Pre-checks using assert
        assert name.strip() != "", "Name cannot be empty."
        assert email.strip() != "", "Email cannot be empty."
        assert password.strip() != "", "Password cannot be empty."

        # Type checks
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")

        # Age validation
        if not age_input.isdigit():
            raise ValueError("Age must be a number.")
        age = int(age_input)
        if age < 13:
            raise ValueError("Age must be 13 or older.")

        # Password strength check
        if len(password) < 6 or password.isdigit() or password.isalpha():
            raise PasswordTooWeakError("Password must be at least 6 characters and contain both letters and numbers.")

    except (ValueError, TypeError, AssertionError, PasswordTooWeakError) as e:
        logging.error("Validation error: %s", e)
        print("Registration Failed:", e)
    else:
        print("\n✅ Registration Successful!")
        print(f"Name: {name}\nEmail: {email}\nAge: {age}")
    finally:
        print("Registration process complete.")

# Run the form
validate_registration()
