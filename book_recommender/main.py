# main.py

from book_ops import create_genre_index, search_books_by_author, search_books_by_genre, display_book
from recommend import recommend_by_genre, recommend_by_author

# Sample books
books = [
    {"id": ("The Alchemist", "Paulo Coelho"), "genres": {"Fiction", "Philosophy"}},
    {"id": ("Brida", "Paulo Coelho"), "genres": {"Fiction", "Spiritual"}},
    {"id": ("Dune", "Frank Herbert"), "genres": {"Sci-Fi", "Adventure"}},
    {"id": ("Neuromancer", "William Gibson"), "genres": {"Sci-Fi", "Cyberpunk"}},
    {"id": ("1984", "George Orwell"), "genres": {"Dystopian", "Fiction"}},
]

# Build genre index
genre_index = create_genre_index(books)

# ---- Search Example ----
print("\n🔍 Books by Paulo Coelho:")
for book in search_books_by_author(books, "Paulo Coelho"):
    print(display_book(book))

print("\n🔍 Books in Sci-Fi genre:")
for book in search_books_by_genre(books, "Sci-Fi"):
    print(display_book(book))

# ---- Recommendations ----
print("\n🎯 Genre-Based Recommendation (Fiction):")
rec = recommend_by_genre(genre_index, "Fiction")
print(display_book(rec) if rec else "No recommendation found.")

print("\n🎯 Author-Based Recommendation (Frank Herbert):")
rec = recommend_by_author(books, "Frank Herbert")
print(display_book(rec) if rec else "No recommendation found.")
