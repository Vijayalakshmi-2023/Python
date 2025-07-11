# Feedback Analyzer

# Step 1: Input list of feedback messages (example list)
messages = [
    "The service was good and quick.",
    "I didn't like the food.",
    "Good ambience and friendly staff.",
    "Could be better.",
    "Had a good experience overall."
]

# Step 2: Analyze each message using for loop
print("----- Feedback Classification -----")
for msg in messages:
    if "good" in msg.lower():  # Case-insensitive check
        category = "Positive"
    else:
        category = "Neutral"
    
    print(f"Message: \"{msg}\" → {category}")
print("-----------------------------------")
