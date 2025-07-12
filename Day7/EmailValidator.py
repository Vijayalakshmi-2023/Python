# Input email
email = input("Enter an email address: ").strip()

# Check if '@' and '.' are present
at_pos = email.find('@')
dot_pos = email.find('.', at_pos)  # look for '.' after '@'

if at_pos == -1 or dot_pos == -1:
    print("Invalid email: missing '@' or '.' after '@'.")
else:
    # Extract username and domain
    username = email[:at_pos]
    domain = email[at_pos+1:]

    # Validate domain exactly "gmail.com"
    if domain != "gmail.com":
        print("Invalid email: domain is not 'gmail.com'.")
    # Validate username length > 5
    elif len(username) <= 5:
        print("Invalid email: username must be longer than 5 characters.")
    else:
        print("Email is valid!")
