# book_ops.py

def add_book(library, title, author, year, genres):
    book_info = (title, author, year)
    book = {
        'info': book_info,
        'available': True,
        'genres': set(genres)
    }
    library.append(book)
    return book

def search_books(library, keyword):
    keyword = keyword.lower()
    return [
        book for book in library
        if keyword in book['info'][0].lower() or keyword in book['info'][1].lower()
    ]

def list_unique_genres(library):
    genre_set = set()
    for book in library:
        genre_set.update(book['genres'])
    return genre_set

def display_book(book):
    title, author, year = book['info']
    genres = ", ".join(book['genres'])
    status = "Available" if book['available'] else "Borrowed"
    return f"{title} by {author} ({year}) | Genres: {genres} | Status: {status}"
