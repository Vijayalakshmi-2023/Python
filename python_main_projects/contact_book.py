import json
import csv
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    category = input("Category (Family/Friends/Work/Other): ").capitalize()
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    })
    print("Contact added successfully.")

def view_contacts(contacts, grouped=False):
    if not contacts:
        print("No contacts found.")
        return

    if grouped:
        categories = {}
        for contact in contacts:
            cat = contact["category"]
            categories.setdefault(cat, []).append(contact)
        for cat, group in categories.items():
            print(f"\n--- {cat.upper()} ---")
            for contact in group:
                print_contact(contact)
    else:
        for contact in contacts:
            print_contact(contact)

def print_contact(contact):
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Category: {contact['category']}")

def search_contacts(contacts):
    term = input("Enter name or phone number to search: ").lower()
    results = [c for c in contacts if term in c['name'].lower() or term in c['phone']]
    
    if results:
        for contact in results:
            print_contact(contact)
    else:
        print("No matching contacts found.")

def edit_contact(contacts):
    search_contacts(contacts)
    name = input("Enter exact name of the contact to edit: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave field blank to keep current value.")
            new_name = input(f"New name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New email ({contact['email']}): ") or contact['email']
            new_category = input(f"New category ({contact['category']}): ") or contact['category']
            
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "category": new_category.capitalize()
            })
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_contacts(contacts)
    name = input("Enter exact name of contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            print("Contact deleted.")
            return
    print("Contact not found.")

def export_to_csv(contacts):
    filename = input("Enter CSV filename (e.g., contacts.csv): ")
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "category"])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    print(f"Contacts exported to {filename}")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. View Contacts by Group")
        print("4. Search Contact")
        print("5. Edit Contact")
        print("6. Delete Contact")
        print("7. Export Contacts to CSV")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            view_contacts(contacts, grouped=True)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            edit_contact(contacts)
        elif choice == '6':
            delete_contact(contacts)
        elif choice == '7':
            export_to_csv(contacts)
        elif choice == '0':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
