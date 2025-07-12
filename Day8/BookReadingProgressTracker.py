# Book Reading Progress Tracker

# Each book: [name, pages_read, total_pages]
books = []

def add_book():
    name = input("Enter book name: ").strip().title()
    try:
        total_pages = int(input("Enter total pages: "))
        books.append([name, 0, total_pages])
        print(f"✅ '{name}' added with 0/{total_pages} pages read.")
    except ValueError:
        print("❌ Invalid number of pages.")

def update_progress():
    name = input("Enter book name to update: ").strip().title()
    for book in books:
        if book[0] == name:
            try:
                new_pages = int(input(f"Enter pages read so far (max {book[2]}): "))
                if 0 <= new_pages <= book[2]:
                    book[1] = new_pages
                    print(f"📖 Updated: {name} → {book[1]}/{book[2]} pages read.")
                else:
                    print("❌ Page count exceeds total pages.")
            except ValueError:
                print("❌ Invalid page number.")
            return
    print("❌ Book not found.")

def check_finished():
    print("\n✅ Finished Books:")
    found = False
    for book in books:
        if book[1] == book[2]:
            print(f"- {book[0]} (Completed)")
            found = True
    if not found:
        print("None yet. Keep reading! 📚")

def display_progress():
    print("\n📊 Reading Progress:")
    if not books:
        print("No books added yet.")
    for book in books:
        status = "✅ Finished" if book[1] == book[2] else "📖 In Progress"
        print(f"{book[0]} → {book[1]}/{book[2]} pages read ({status})")

def main():
    while True:
        print("\n📚 Book Reading Progress Tracker")
        print("1. Add new book")
        print("2. Update reading progress")
        print("3. Check finished books")
        print("4. View all reading progress")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            update_progress()
        elif choice == "3":
            check_finished()
        elif choice == "4":
            display_progress()
        elif choice == "5":
            print("📕 Exiting Tracker. Happy reading!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
