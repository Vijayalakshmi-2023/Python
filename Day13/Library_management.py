from datetime import date, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn})"

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    @abstractmethod
    def get_role(self):
        pass

class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.__borrowed_books = []

    def get_role(self):
        return "Member"

    def borrow_book(self, book, due_date):
        self.__borrowed_books.append((book, due_date))

    def return_book(self, book):
        self.__borrowed_books = [b for b in self.__borrowed_books if b[0] != book]

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __str__(self):
        return f"{self.name} ({self.get_role()})"

class Librarian(Person):
    def get_role(self):
        return "Librarian"

    def __str__(self):
        return f"{self.name} ({self.get_role()})"

class Transaction:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = date.today()
        self.due_date = self.borrow_date + timedelta(days=14)

    def __str__(self):
        return f"{self.member.name} borrowed '{self.book.get_title()}' on {self.borrow_date}, due by {self.due_date}"

class Library:
    def __init__(self):
        self.__books = []
        self.__members = []
        self.__transactions = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, isbn):
        self.__books = [b for b in self.__books if b.get_isbn() != isbn]

    def search_book(self, keyword):
        return [book for book in self.__books if keyword.lower() in book.get_title().lower()]

    def register_member(self, member):
        self.__members.append(member)

    def borrow_book(self, member, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn and not book.is_borrowed:
                book.is_borrowed = True
                transaction = Transaction(member, book)
                self.__transactions.append(transaction)
                member.borrow_book(book, transaction.due_date)
                return f"Book '{book.get_title()}' issued to {member.name}."
        return "Book not available."

    def return_book(self, member, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn and book.is_borrowed:
                book.is_borrowed = False
                member.return_book(book)
                return f"Book '{book.get_title()}' returned by {member.name}."
        return "Book not found or not issued."

    def view_transactions(self):
        for t in self.__transactions:
            print(t)

    def __len__(self):
        return len(self.__books)

# Setup
lib = Library()
lib.add_book(Book("Python Programming", "Guido", "12345"))
lib.add_book(Book("OOP with Python", "James", "54321"))

member = Member("Anil", "M001")
librarian = Librarian("Sita", "L001")

lib.register_member(member)

# Borrow
print(lib.borrow_book(member, "12345"))
print()

# View borrowed books
for b, due in member.get_borrowed_books():
    print(f"{b.get_title()} (Due: {due})")

# Return
print()
print(lib.return_book(member, "12345"))

# Search
print()
results = lib.search_book("python")
for r in results:
    print(r)

# Length
print()
print("Total books in library:", len(lib))

# View Transactions
print("\nTransactions:")
lib.view_transactions()
