
# lending_ops.py

from datetime import datetime

books = {}  # title → (borrower, due_date)
borrowers = set()

def borrow_book(title, borrower, due_date_str):
    if title in books:
        return f"❌ '{title}' is already borrowed."

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        return "❌ Invalid date format. Use YYYY-MM-DD."

    books[title] = (borrower, due_date)
    borrowers.add(borrower)
    return f"✅ '{title}' borrowed by {borrower} until {due_date}."

def return_book(title):
    if title in books:
        borrower, _ = books.pop(title)
        return f"✅ '{title}' returned by {borrower}."
    return f"❌ '{title}' is not currently borrowed."

def list_borrowed_books():
    if not books:
        return "📚 No books are currently borrowed."
    output = "📖 Borrowed Books:\n"
    for title, (borrower, due_date) in books.items():
        output += f"- {title} → {borrower} (due {due_date})\n"
    return output
