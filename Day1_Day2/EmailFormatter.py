def format_email():
    sender = input("Enter your name: ").strip()
    recipient = input("Enter recipient's email: ").strip()
    subject = input("Enter subject: ").strip()
    print("Enter your message (type END on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    message = "\n".join(lines)

    email = f"""
From: {sender}
To: {recipient}
Subject: {subject}

{message}

Best regards,
{sender}
"""
    print("\n--- Formatted Email ---")
    print(email)

if __name__ == "__main__":
    format_email()
