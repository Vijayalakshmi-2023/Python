# user_ops.py

def borrow_book(library, title):
    for book in library:
        if book['info'][0].lower() == title.lower() and book['available']:
            book['available'] = False
            return f"You have borrowed: {book['info'][0]}"
    return "Book not available or already borrowed."

def return_book(library, title):
    for book in library:
        if book['info'][0].lower() == title.lower() and not book['available']:
            book['available'] = True
            return f"You have returned: {book['info'][0]}"
    return "Book not found or not borrowed."
