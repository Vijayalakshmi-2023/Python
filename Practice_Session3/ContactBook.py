# Contact Book App

# Each contact is stored as: [name, phone, email]
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append([name, phone, email])
    print(f"✅ Contact '{name}' added.\n")

# Function to show all contacts
def show_all_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\n=== All Contacts ===")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    print()

# Function to search for a contact
def search_contact():
    keyword = input("Enter name/phone/email to search: ").strip().lower()
    found = False

    print("\n=== Search Results ===")
    for contact in contacts:
        if any(keyword in field.lower() for field in contact):
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            found = True

    if not found:
        print("No matching contact found.\n")
    else:
        print()

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the exact name of the contact to delete: ").strip()
    for contact in contacts:
        if contact[0].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print(f"🗑️ Contact '{contact[0]}' deleted.\n")
            return
    print("Contact not found.\n")

# Main menu loop
def main():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
