correct_otp = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_otp = input("Enter OTP: ").strip()
    if entered_otp == correct_otp:
        print("✅ OTP verified successfully!")
        break
    else:
        print("❌ Incorrect OTP. Try again.")
        attempts += 1
else:
    print("❌ OTP failed after 3 attempts.")
