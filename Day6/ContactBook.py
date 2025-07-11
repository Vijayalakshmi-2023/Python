# Global contact dictionary
contacts = {}

# Function to add a new contact
def add_contact(**kwargs):
    global contacts
    name = kwargs.get('name')
    if not name:
        return "❌ Contact must have a name."

    contacts[name.lower()] = {
        "Phone": kwargs.get('phone', 'N/A'),
        "Email": kwargs.get('email', 'N/A'),
        "Address": kwargs.get('address', 'N/A')
    }
    return f"✅ Contact '{name}' added successfully."

# Function to return sorted contact names
def list_contacts():
    return sorted(contacts.keys())

# Function to search and return contact details
def search_contact(name):
    return contacts.get(name.lower(), "❌ Contact not found.")

# --- Example Usage ---
print(add_contact(name="Alice", phone="1234567890", email="alice@example.com"))
print(add_contact(name="Bob", phone="9876543210"))
print(add_contact(name="Charlie", email="charlie@example.com", address="Downtown Street"))

print("\n📇 Sorted Contact List:")
print(list_contacts())

print("\n🔍 Search Result for 'Bob':")
print(search_contact("Bob"))

print("\n🔍 Search Result for 'Diana':")
print(search_contact("Diana"))
