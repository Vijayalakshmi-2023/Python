# Format: {book_id: {"title": ..., "author": ..., "copies": ...}}
library = {}
# Add a new book
def add_book(book_id, title, author, copies):
    if book_id not in library:
        library[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book '{title}' added.")
    else:
        print(f"Book ID {book_id} already exists.")

# Borrow a book (reduce copies)
def borrow_book(book_id):
    book = library.get(book_id)
    if book and book["copies"] > 0:
        book["copies"] -= 1
        print(f"You borrowed '{book['title']}'.")
        if book["copies"] == 0:
            print(f"'{book['title']}' is now out of stock and will be removed.")
            library.pop(book_id)
    else:
        print("Book not available.")

# Return a book (increase copies)
def return_book(book_id, title=None, author=None):
    book = library.get(book_id)
    if book:
        book["copies"] += 1
        print(f"You returned '{book['title']}'.")
    else:
        # Optionally re-add if it was deleted
        if title and author:
            library[book_id] = {"title": title, "author": author, "copies": 1}
            print(f"Returned book '{title}' re-added to library.")
        else:
            print("Book ID not found. Cannot return without title/author info.")

# Display all available books using .items()
def show_books():
    print("\nAvailable Books:")
    if not library:
        print("  No books in the catalog.")
    for book_id, info in library.items():
        print(f"  ID: {book_id} | Title: {info['title']} | Author: {info['author']} | Copies: {info['copies']}")

# Add books
add_book(101, "1984", "George Orwell", 3)
add_book(102, "To Kill a Mockingbird", "Harper Lee", 2)
add_book(103, "The Great Gatsby", "F. Scott Fitzgerald", 1)

# Borrow books
borrow_book(101)
borrow_book(103)  # Will go to 0 copies and be removed

# Return books
return_book(101)
return_book(103, "The Great Gatsby", "F. Scott Fitzgerald")

# Display books
show_books()
