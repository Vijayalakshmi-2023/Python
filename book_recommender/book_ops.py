# book_ops.py

def create_genre_index(books):
    genre_index = {}
    for book in books:
        for genre in book["genres"]:
            genre_index.setdefault(genre, []).append(book)
    return genre_index

def search_books_by_author(books, author):
    return [book for book in books if book["id"][1].lower() == author.lower()]

def search_books_by_genre(books, genre):
    return [book for book in books if genre in book["genres"]]

def display_book(book):
    title, author = book["id"]
    genres = ", ".join(book["genres"])
    return f"📘 {title} by {author} [{genres}]"
