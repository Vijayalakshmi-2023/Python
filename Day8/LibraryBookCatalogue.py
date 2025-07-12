# Library Book Catalog
catalog = [
    ["1984", "George Orwell"],
    ["To Kill a Mockingbird", "Harper Lee"],
    ["The Great Gatsby", "F. Scott Fitzgerald"]
]

def show_menu():
    print("\n📚 Library Catalog Menu")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Update book details")
    print("5. Search for a book by title")
    print("6. Show recent additions (last 3)")
    print("7. Exit")

def view_books():
    if not catalog:
        print("No books in the catalog.")
    else:
        print("\n📖 Book List:")
        for title, author in catalog:
            print(f"Title: {title}, Author: {author}")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    catalog.append([title, author])
    print(f"✅ Book '{title}' by {author} added.")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in catalog:
        if book[0].lower() == title.lower():
            catalog.remove(book)
            print(f"🗑️ Book '{title}' removed.")
            return
    print(f"❌ Book '{title}' not found.")

def update_book():
    title = input("Enter the title of the book to update: ").strip()
    for book in catalog:
        if book[0].lower() == title.lower():
            new_title = input("Enter new title: ").strip()
            new_author = input("Enter new author: ").strip()
            book[0] = new_title
            book[1] = new_author
            print(f"🔄 Book updated to '{new_title}' by {new_author}.")
            return
    print(f"❌ Book '{title}' not found.")

def search_book():
    title = input("Enter the title to search: ").strip()
    titles = [book[0].lower() for book in catalog]
    if title.lower() in titles:
        index = titles.index(title.lower())
        book = catalog[index]
        print(f"✅ Found: '{book[0]}' by {book[1]}")
    else:
        print(f"❌ Book '{title}' not found.")

def show_recent_additions():
    print("\n🆕 Recent Additions:")
    for book in catalog[-3:]:  # Slicing last 3
        print(f"Title: {book[0]}, Author: {book[1]}")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–7): ")

    if choice == "1":
        view_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        show_recent_additions()
    elif choice == "7":
        print("Exiting Library Catalog. Goodbye! 📕")
        break
    else:
        print("Invalid choice. Please try again.")
