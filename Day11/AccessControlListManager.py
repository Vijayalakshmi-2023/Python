# Access Control List Manager

# Define sets of users for each role
admins = {"alice", "bob", "carol"}
editors = {"bob", "dave"}
viewers = {"eve", "frank", "alice"}

# Check if editors are subset of admins (all editors are admins)
if editors.issubset(admins):
    print("All editors have admin access.")
else:
    print("Some editors do NOT have admin access.")

# Check if admins are superset of editors (admins include all editors)
if admins.issuperset(editors):
    print("Admins include all editors.")
else:
    print("Admins do NOT include all editors.")

# Check for conflicting roles (no overlap between editors and viewers)
if editors.isdisjoint(viewers):
    print("No conflicting roles between editors and viewers.")
else:
    print("There are users with both editor and viewer roles!")

# Example outputs
print("\nAdmins:", admins)
print("Editors:", editors)
print("Viewers:", viewers)
