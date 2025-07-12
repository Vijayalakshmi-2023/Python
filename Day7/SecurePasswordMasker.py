# Input password from user
password = input("Enter your password: ")

# Check if password is long enough to mask
if len(password) <= 2:
    # Not enough characters to mask
    masked_password = password
else:
    first_char = password[0]
    last_char = password[-1]
    middle = "*" * (len(password) - 2)
    masked_password = first_char + middle + last_char

# Output masked password
print("Masked password:", masked_password)
