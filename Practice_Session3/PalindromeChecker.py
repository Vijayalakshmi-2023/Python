# Function to check if a word or sentence is a palindrome
def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())  # remove spaces and punctuation
    return cleaned == cleaned[::-1]

# Main loop
def main():
    print("=== Palindrome Checker ===")
    while True:
        user_input = input("Enter a word or sentence (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("👋 Goodbye!")
            break

        if is_palindrome(user_input):
            print("✅ It's a palindrome!\n")
        else:
            print("❌ Not a palindrome.\n")

# Run the checker
main()
