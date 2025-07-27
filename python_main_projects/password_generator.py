import random
import string
import os
from cryptography.fernet import Fernet

# Generate a key for encryption if none exists
def generate_key():
    return Fernet.generate_key()

# Save key to a file (only if it doesn't exist)
def save_key(key, filename='password_key.key'):
    if not os.path.exists(filename):
        with open(filename, 'wb') as key_file:
            key_file.write(key)

# Load key from a file
def load_key(filename='password_key.key'):
    return open(filename, 'rb').read()

# Encrypt passwords before saving
def encrypt_passwords(passwords, key):
    f = Fernet(key)
    encrypted_passwords = [f.encrypt(p.encode()).decode() for p in passwords]
    return encrypted_passwords

# Password strength checker
def password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

# Password generation function
def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True, use_lowercase=True):
    if not any([use_symbols, use_numbers, use_uppercase, use_lowercase]):
        raise ValueError("At least one character type must be selected.")
    
    char_set = ''
    if use_symbols:
        char_set += string.punctuation
    if use_numbers:
        char_set += string.digits
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

# Main password generator function
def generate_passwords():
    # Get user input
    num_passwords = int(input("How many passwords to generate? "))
    length = int(input("Password length: "))
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
        strength = password_strength(password)
        print(f"Password: {password} | Strength: {strength}")
        passwords.append(password)
    
    return passwords

def save_passwords_to_file(passwords, filename="passwords.txt"):
    key = generate_key()  # Generate a new encryption key
    save_key(key)  # Save the key to a file
    encrypted_passwords = encrypt_passwords(passwords, key)
    
    with open(filename, 'w') as f:
        for ep in encrypted_passwords:
            f.write(f"{ep}\n")
    
    print(f"Passwords saved to {filename}.")

# Main program flow
def main():
    print("=== Password Generator ===")
    passwords = generate_passwords()

    # Ask if user wants to save passwords
    save = input("Do you want to save the passwords to a file? (y/n): ").lower()
    if save == 'y':
        save_passwords_to_file(passwords)

if __name__ == '__main__':
    main()
