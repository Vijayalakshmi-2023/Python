role = input("Enter your role (admin/user): ").strip().lower()
has_id = input("Do you have an ID? (yes/no): ").strip().lower()
if role in ["admin", "user"]:
    if has_id == "yes" and not (role == "user" and has_id != "yes"):
        print(f"✅ Access granted to {role}.")
    else:
        print("❌ Access denied. ID required.")
else:
    print("❌ Invalid role. Access denied.")
