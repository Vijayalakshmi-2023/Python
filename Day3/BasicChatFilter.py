banned_words = ["badword", "spam", "fake", "scam", "hate"]

message = input("Enter your message: ").lower() 

if any(word in message for word in banned_words):
    print("⚠️ Warning: Your message contains banned words and cannot be sent.")
else:
    print("✅ Message sent successfully.")
