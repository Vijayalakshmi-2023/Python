# Initial list of books available
books = [
    "1984 by George Orwell",
    "To Kill a Mockingbird by Harper Lee",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Pride and Prejudice by Jane Austen",
    "The Hobbit by J.R.R. Tolkien"
]

# Show available books
def show_books():
    if books:
        print("\n📚 Available Books:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")
    else:
        print("\n📭 No books currently available.")

# Borrow a book
def borrow_book():
    show_books()
    if not books:
        return
    try:
        choice = int(input("\nEnter book number to borrow: "))
        if 1 <= choice <= len(books):
            borrowed = books.pop(choice - 1)
            print(f"✅ You borrowed: '{borrowed}'\n")
        else:
            print("❌ Invalid book number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Return a book
def return_book():
    book_name = input("\nEnter the name of the book to return: ").strip()
    if book_name:
        books.append(book_name)
        print(f"📥 '{book_name}' returned. Thank you!\n")
    else:
        print("❌ Book name cannot be empty.\n")

# Main menu loop
def main():
    while True:
        print("=== Book Lending App ===")
        print("1. Show Available Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
