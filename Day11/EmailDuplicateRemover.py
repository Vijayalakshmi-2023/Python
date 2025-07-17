# Email Duplicate Remover

# List of contacts with duplicates
imported_contacts = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com",
    "david@example.com"
]

# Convert list to set to remove duplicates
unique_contacts_set = set(imported_contacts)

# Convert the set back to a list for further use
cleaned_contacts = list(unique_contacts_set)

print("Cleaned contact list (duplicates removed):")
print(cleaned_contacts)

# Check if a certain email is present
email_to_check = "charlie@example.com"
if email_to_check in unique_contacts_set:
    print(f"\nEmail '{email_to_check}' is in the contact list.")
else:
    print(f"\nEmail '{email_to_check}' is NOT in the contact list.")
