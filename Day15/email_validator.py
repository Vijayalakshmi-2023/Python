class InvalidEmailFormatError(Exception):
    """Raised when an email format is invalid."""
    pass
import re
import logging

# Setup logging
logging.basicConfig(filename='invalid_emails.log', level=logging.WARNING, format='%(asctime)s - %(message)s')

def validate_email(email):
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailFormatError(f"Invalid email format: {email}")
def process_emails(email_list):
    valid_emails = []
    for email in email_list:
        try:
            validate_email(email)
            print(f"✅ Valid: {email}")
            valid_emails.append(email)
        except InvalidEmailFormatError as e:
            print(f"❌ {e}")
            logging.warning(str(e))
    return valid_emails
if __name__ == "__main__":
    emails = input("Enter emails separated by commas: ").split(",")
    emails = [email.strip() for email in emails]
    
    print("\nValidating Emails...\n")
    valid_list = process_emails(emails)

    print("\n✅ Final Valid Emails:")
    for e in valid_list:
        print("-", e)
