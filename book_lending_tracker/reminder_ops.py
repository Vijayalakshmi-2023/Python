# reminder_ops.py

from datetime import date
from lending_ops import books

def get_overdue_books():
    today = date.today()
    overdue = {title: (borrower, due_date) for title, (borrower, due_date) in books.items() if due_date < today}
    return overdue

def send_reminders():
    overdue_books = get_overdue_books()
    if not overdue_books:
        return "✅ No overdue books today."
    
    message = "📢 Overdue Book Reminders:\n"
    for title, (borrower, due_date) in overdue_books.items():
        message += f"- '{title}' borrowed by {borrower} was due on {due_date}.\n"
    return message
