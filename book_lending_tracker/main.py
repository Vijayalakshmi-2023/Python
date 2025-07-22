# main.py

from lending_ops import borrow_book, return_book, list_borrowed_books
from reminder_ops import send_reminders

def main():
    while True:
        print("\n📚 Book Lending Tracker")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. View Borrowed Books")
        print("4. Send Reminders")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ").strip()
            borrower = input("Enter borrower name: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            print(borrow_book(title, borrower, due_date))

        elif choice == "2":
            title = input("Enter book title to return: ").strip()
            print(return_book(title))

        elif choice == "3":
            print(list_borrowed_books())

        elif choice == "4":
            print(send_reminders())

        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
