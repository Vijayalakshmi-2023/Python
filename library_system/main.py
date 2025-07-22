# main.py

from book_ops import add_book, search_books, list_unique_genres, display_book
from user_ops import borrow_book, return_book

# Initialize library
library = []

# Add books
add_book(library, "1984", "George Orwell", 1949, {"Dystopian", "Political"})
add_book(library, "The Hobbit", "J.R.R. Tolkien", 1937, {"Fantasy", "Adventure"})
add_book(library, "Python Basics", "Jane Doe", 2020, {"Education", "Programming"})

# Display all books
print("Library Collection:\n")
for book in library:
    print(display_book(book))

# Borrow a book
print("\nBorrowing 'The Hobbit':")
print(borrow_book(library, "The Hobbit"))

# Try to borrow again
print(borrow_book(library, "The Hobbit"))

# Return a book
print("\nReturning 'The Hobbit':")
print(return_book(library, "The Hobbit"))

# Search by title/author
print("\nSearch results for 'python':")
results = search_books(library, "python")
for book in results:
    print(display_book(book))

# Show unique genres
print("\nAll Unique Genres:")
print(", ".join(list_unique_genres(library)))

