# main.py

from storage_ops import load_entries, save_entries
from search_ops import search_by_date, search_by_tag, summary

def input_tags():
    return set(input("Enter tags (comma-separated): ").lower().split(','))

def display(entry):
    print(f"\n🗓 {entry['date']}")
    print(f"📌 Tags: {', '.join(entry['tags'])}")
    print(f"📝 {entry['text']}\n")

def main():
    entries = load_entries()

    while True:
        print("\n--- Personal Diary ---")
        print("1. Add Entry")
        print("2. Edit Entry")
        print("3. Delete Entry")
        print("4. Search by Date")
        print("5. Search by Tag")
        print("6. Summary")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            text = input("Entry text: ")
            tags = input_tags()
            entries.append({'date': date, 'text': text, 'tags': tags})
            save_entries(entries)
            print("✅ Entry added.")

        elif choice == "2":
            date = input("Enter date of entry to edit: ")
            matches = search_by_date(entries, date)
            if matches:
                new_text = input("New text: ")
                new_tags = input_tags()
                matches[0]['text'] = new_text
                matches[0]['tags'] = new_tags
                save_entries(entries)
                print("✅ Entry updated.")
            else:
                print("❌ Entry not found.")

        elif choice == "3":
            date = input("Enter date of entry to delete: ")
            entries = [e for e in entries if e['date'] != date]
            save_entries(entries)
            print("✅ Entry deleted.")

        elif choice == "4":
            date = input("Search date (YYYY-MM-DD): ")
            found = search_by_date(entries, date)
            for e in found:
                display(e)
            if not found:
                print("❌ No entry found.")

        elif choice == "5":
            tag = input("Search tag: ").strip().lower()
            found = search_by_tag(entries, tag)
            for e in found:
                display(e)
            if not found:
                print("❌ No entries with that tag.")

        elif choice == "6":
            total, tags = summary(entries)
            print(f"\n📖 Total entries: {total}")
            print(f"🏷 Unique tags: {', '.join(tags)}")

        elif choice == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
