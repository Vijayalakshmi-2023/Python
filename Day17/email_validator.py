import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

def email_validator(email_list):
    valid_count = 0
    for email in email_list:
        if is_valid_email(email):
            yield email
            valid_count += 1
            if valid_count == 10:
                return  # Raises StopIteration
emails = [
    "jeeva@example.com", "invalid@.com", "joe.doe@mail.org",
    "bademail@", "user123@host.net", "hello@domain", "me@web.dev",
    "wrong@domain,com", "first.last@edu.in", "test123@ok.co",
    "valid@yes.com", "extra@more.com"
]

for e in email_validator(emails):
    print("✅", e)
