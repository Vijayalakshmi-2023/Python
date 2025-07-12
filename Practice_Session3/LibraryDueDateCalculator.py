from datetime import datetime, timedelta

def get_borrow_date():
    while True:
        date_str = input("Enter borrow date (YYYY-MM-DD): ").strip()
        try:
            borrow_date = datetime.strptime(date_str, "%Y-%m-%d")
            return borrow_date
        except ValueError:
            print("❌ Invalid date format. Please enter as YYYY-MM-DD.")

def calculate_due_date(borrow_date, days=7):
    return borrow_date + timedelta(days=days)

def display_summary(book_name, borrow_date, due_date):
    print("\n=== Book Borrow Summary ===")
    print(f"📖 Book: {book_name}")
    print(f"📅 Borrow Date: {borrow_date.strftime('%Y-%m-%d')}")
    print(f"⏳ Due Date: {due_date.strftime('%Y-%m-%d')}\n")

def main():
    print("=== Library Due Date Calculator ===")
    book_name = input("Enter book name: ").strip()
    borrow_date = get_borrow_date()
    due_date = calculate_due_date(borrow_date)
    display_summary(book_name, borrow_date, due_date)

if __name__ == "__main__":
    main()
