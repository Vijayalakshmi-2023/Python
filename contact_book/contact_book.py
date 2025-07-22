# contact_book.py

import json
from collections import defaultdict

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, tags):
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "tags": tuple(tags)  # Categories stored as immutable tuple
        }

    def update_contact(self, name, phone=None, email=None, tags=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if tags:
                self.contacts[name]["tags"] = tuple(tags)

    def delete_contact(self, name):
        return self.contacts.pop(name, None)

    def search_contact(self, name):
        return self.contacts.get(name)

    def list_contacts(self):
        return sorted(self.contacts.items())

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.contacts, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.contacts = json.load(f)
                # Convert tags back to tuple
                for contact in self.contacts.values():
                    contact['tags'] = tuple(contact['tags'])
        except FileNotFoundError:
            pass
