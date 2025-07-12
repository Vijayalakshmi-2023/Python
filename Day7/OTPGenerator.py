import random
import string

# Input mobile number
mobile = input("Enter your mobile number: ").strip()

# Extract last 4 digits (handle if less than 4 digits)
last4 = mobile[-4:] if len(mobile) >= 4 else mobile

# Generate 2 random uppercase letters
random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))

# Generate OTP: last4 digits + 2 random letters mixed
# Let's shuffle the characters for a better OTP

otp_chars = list(last4 + random_letters)
random.shuffle(otp_chars)
otp = ''.join(otp_chars)

print("\nGenerated OTP:", otp)
