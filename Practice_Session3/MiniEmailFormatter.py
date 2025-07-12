def format_email(name, domain):
    # Clean and format name: lowercase, replace spaces with dots
    username = name.strip().lower().replace(" ", ".")
    # Clean domain (lowercase, strip spaces)
    domain = domain.strip().lower()
    # Combine to form email
    email = f"{username}@{domain}"
    return email

def main():
    print("=== Mini Email Formatter ===")
    name = input("Enter full name: ")
    domain = input("Enter email domain (e.g., example.com): ")

    email = format_email(name, domain)
    print(f"\n📧 Generated Email: {email}")

if __name__ == "__main__":
    main()
