# Input CSV string
csv_input = input("Enter items separated by commas: ")

# Split items and strip spaces
items = [item.strip() for item in csv_input.split(",")]

# Format sentence
if len(items) == 0:
    sentence = "You bought nothing."
elif len(items) == 1:
    sentence = f"You bought {items[0]}."
elif len(items) == 2:
    sentence = f"You bought {items[0]} and {items[1]}."
else:
    # Join all except last with comma, add 'and' before last
    sentence = "You bought " + ", ".join(items[:-1]) + ", and " + items[-1] + "."

print("\n" + sentence)
