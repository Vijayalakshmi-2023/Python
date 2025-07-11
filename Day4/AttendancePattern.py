# Attendance Pattern with Pass

# List of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Process attendance
for day in days:
    if day == "Sunday":
        pass  # Reserved for future logic
    else:
        print(f"{day}: Marked Present")
