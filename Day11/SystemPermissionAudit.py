# System Permissions Audit

# Required permissions for a critical system feature
required_permissions = {"read", "write", "execute", "admin"}

# Permissions assigned to different users
user_permissions = {
    "Alice": {"read", "write", "execute", "admin"},
    "Bob": {"read", "write"},
    "Charlie": {"read", "execute"},
    "David": {"read", "write", "execute"},
}

for user, perms in user_permissions.items():
    if required_permissions.issubset(perms):
        print(f"{user} has all required permissions.")
    else:
        missing = required_permissions.difference(perms)
        print(f"{user} is missing permissions: {missing}")
