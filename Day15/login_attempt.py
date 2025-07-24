import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='login_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class LoginFailedError(Exception):
    pass

# Dummy credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret123"

def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if not username or not password:
                raise ValueError("Username and password cannot be empty.")

            if username == VALID_USERNAME and password == VALID_PASSWORD:
                print("\n✅ Login successful!")
                return

            else:
                raise ValueError("Invalid username or password.")

        except ValueError as ve:
            attempts += 1
            logging.error("Login attempt %d failed: %s", attempts, ve)
            print(f"❌ Attempt {attempts}/{max_attempts} failed: {ve}")

        except Exception as e:
            attempts += 1
            logging.error("Unexpected error on attempt %d: %s", attempts, e)
            print(f"❌ Attempt {attempts}/{max_attempts} failed: Unexpected error")

    # After 3 failed attempts
    raise LoginFailedError("Maximum login attempts exceeded.")

# Run the login system
try:
    login()
except LoginFailedError as e:
    logging.error(e)
    print("🚫", e)
