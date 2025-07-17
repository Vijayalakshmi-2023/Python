# Book Club Member Organizer

# Members of two book clubs
club_a = {"Alice", "Bob", "Charlie", "David"}
club_b = {"Charlie", "Eva", "Frank", "Alice"}

# Find common members (in both clubs)
common_members = club_a.intersection(club_b)
print("Common members:", common_members)

# Find members exclusive to one club or the other (not both)
exclusive_members = club_a.symmetric_difference(club_b)
print("Exclusive members:", exclusive_members)
