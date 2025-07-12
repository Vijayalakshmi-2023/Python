print("Enter your multi-line quote (finish input with a blank line):")

# Collect multi-line input
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Join lines with newline characters to mimic triple-quoted string
quote = "\n".join(lines).strip()

# Count how many lines based on '\n'
line_count = quote.count("\n") + 1 if quote else 0

print("\nYour saved quote:")
print(quote)
print(f"\nTotal lines in the quote: {line_count}")
