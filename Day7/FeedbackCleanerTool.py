# Input feedback from user
feedback = input("Enter your feedback: ")

# Clean extra spaces
cleaned_feedback = feedback.strip()

# Remove all exclamation marks '!'
cleaned_feedback = cleaned_feedback.replace("!", "")

# Count words (split by spaces)
word_count = len(cleaned_feedback.split())

# Count characters (excluding leading/trailing spaces)
char_count = len(cleaned_feedback)

# Output cleaned feedback and counts
print("\nCleaned Feedback:")
print(cleaned_feedback)
print(f"\nWord count: {word_count}")
print(f"Character count: {char_count}")
