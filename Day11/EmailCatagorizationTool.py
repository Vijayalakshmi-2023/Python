# Email Categorization Tool

# Sample email contents with hashtags/topics
emails = [
    "Meeting notes #projectX #deadline",
    "Reminder: submit your timesheets #HR #deadline",
    "Team outing plans #fun #team",
    "ProjectX update and next steps #projectX #update",
]

# Extract hashtags from emails using set comprehension
tags = {word for email in emails for word in email.split() if word.startswith("#")}

# Display unique tags as a single string
tags_string = ', '.join(sorted(tags))

print("Unique tags extracted from emails:")
print(tags_string)
