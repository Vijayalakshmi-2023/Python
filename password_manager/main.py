# main.py

from account_ops import (
    add_account, update_account, delete_account,
    search_by_tag, search_by_site, format_account
)
from password_gen import generate_password

accounts = {}

# Example usage
print("🔐 Simple Password Manager\n")

# Add accounts
print(add_account(accounts, "gmail.com", "user@gmail.com", "secret123", {"email", "personal"}))
print(add_account(accounts, "github.com", "devuser", generate_password(), {"code", "work"}))

# Update
print(update_account(accounts, "gmail.com", password="newpass456"))

# Search by tag
tagged = search_by_tag(accounts, "work")
print("\n🔍 Accounts tagged 'work':")
for site, info in tagged.items():
    print(format_account(site, info))

# Search by site
print("\n🔍 Search for 'github.com':")
info = search_by_site(accounts, "github.com")
if info:
    print(format_account("github.com", info))

# Delete account
print(delete_account(accounts, "gmail.com"))

# View all
print("\n📄 All accounts:")
for site, info in accounts.items():
    print(format_account(site, info))
