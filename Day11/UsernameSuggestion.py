# Username Suggestion System

# Set of usernames already taken
taken_usernames = {"alice", "bob123", "charlie", "delta"}

# New username suggestions to check
new_suggestions = ["echo", "bob123", "foxtrot", "alice", "golf"]

# Valid and unique suggestions will be stored here
valid_unique_suggestions = set()

for username in new_suggestions:
    if username in taken_usernames:
        print(f"Username '{username}' is already taken.")
    else:
        valid_unique_suggestions.add(username)
        taken_usernames.add(username)  # Add to taken to avoid future duplicates
        print(f"Username '{username}' is available and added.")

print("\nValid unique username suggestions:", valid_unique_suggestions)
