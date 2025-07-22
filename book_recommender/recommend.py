# recommend.py

import random

def recommend_by_genre(genre_index, genre, exclude_ids=set()):
    books = genre_index.get(genre, [])
    options = [book for book in books if book["id"] not in exclude_ids]
    if not options:
        return None
    return random.choice(options)

def recommend_by_author(books, author, exclude_ids=set()):
    options = [book for book in books if book["id"][1].lower() == author.lower()
               and book["id"] not in exclude_ids]
    if not options:
        return None
    return random.choice(options)
