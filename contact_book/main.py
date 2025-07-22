# main.py

from contact_book import ContactBook
import validator

def get_contact_details():
    name = input("Name: ").strip()
    while not validator.validate_name(name):
        name = input("Invalid name. Enter again: ").strip()

    phone = input("Phone: ").strip()
    while not validator.validate_phone(phone):
        phone = input("Invalid phone. Enter again: ").strip()

    email = input("Email: ").strip()
    while not validator.validate_email(email):
        email = input("Invalid email. Enter again: ").strip()

    tags = set(input("Tags (comma-separated): ").split(","))
    return name, phone, email, tags

def main():
    book = ContactBook()
    book.load_from_file("contacts_data.txt")

    while True:
        print("\nOptions: [1] Add [2] Update [3] Delete [4] Search [5] List [6] Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            name, phone, email, tags = get_contact_details()
            book.add_contact(name, phone, email, tags)
        elif choice == '2':
            name = input("Enter name to update: ").strip()
            if book.search_contact(name):
                phone = input("New phone (leave blank to skip): ").strip()
                email = input("New email (leave blank to skip): ").strip()
                tags = input("New tags (comma-separated, blank to skip): ").strip()
                book.update_contact(
                    name,
                    phone if phone else None,
                    email if email else None,
                    set(tags.split(",")) if tags else None
                )
            else:
                print("Contact not found.")
        elif choice == '3':
            name = input("Enter name to delete: ").strip()
            if book.delete_contact(name):
                print("Deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter name to search: ").strip()
            contact = book.search_contact(name)
            print(contact if contact else "Contact not found.")
        elif choice == '5':
            for name, details in book.list_contacts():
                print(f"{name} - Phone: {details['phone']}, Email: {details['email']}, Tags: {details['tags']}")
        elif choice == '6':
            book.save_to_file("contacts_data.txt")
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
