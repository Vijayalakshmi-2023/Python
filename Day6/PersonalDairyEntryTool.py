def diary_entry_tool(entry, save_to_file=False):
    def handle_entry():
        if save_to_file:
            with open("diary.txt", "a") as file:
                file.write(entry + "\n\n")
            print("✅ Entry saved to 'diary.txt'")
        else:
            print("\n📝 Diary Entry:")
            print(entry)

    # Call the inner function
    handle_entry()

    # Calculate length and word count
    entry_length = len(entry)
    word_count = len(entry.split())

    return entry_length, word_count

# --- Example Usage ---
user_input = input("Write your diary entry: ")
length, words = diary_entry_tool(user_input, save_to_file=False)

print(f"\n📊 Entry Stats: {words} words, {length} characters")
