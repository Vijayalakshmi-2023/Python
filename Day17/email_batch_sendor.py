def email_sender(emails):
    total_sent = 0
    batch_size = 1  # Default batch size
    try:
        i = 0
        while i < len(emails):
            for _ in range(batch_size):
                if i >= len(emails):
                    break
                yield emails[i]
                total_sent += 1
                i += 1
            # Wait for new batch size via .send()
            batch_size = yield
            if batch_size is None:
                batch_size = 1
    except Exception as e:
        print(f"[ERROR] Sending failed: {e}")
    return f"All {total_sent} emails sent."
email_list = [
    "user1@example.com",
    "user2@example.com",
    "user3@example.com",
    "user4@example.com",
    "user5@example.com"
]
gen = email_sender(email_list)
next(gen)  # Prime the generator

try:
    while True:
        for _ in range(2):  # Simulate 2 emails per batch
            email = gen.send(2)
            print(f"Sending to: {email}")
        # Simulate an error after a few emails
        if email == "user3@example.com":
            gen.throw(Exception("SMTP failure"))
except StopIteration as e:
    print("\nBatch complete.")
    print("Result:", e.value)
