unique_visitors = set()

def add_visitor():
    visitor_id = input("Enter visitor ID or name: ").strip()
    if visitor_id in unique_visitors:
        print(f"Visitor '{visitor_id}' has already visited.")
    else:
        unique_visitors.add(visitor_id)
        print(f"Visitor '{visitor_id}' added.")

def show_count():
    print(f"Total unique visitors: {len(unique_visitors)}")

def main():
    while True:
        print("\nUnique Visitor Counter")
        print("1. Add Visitor")
        print("2. Show Unique Visitor Count")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_visitor()
        elif choice == '2':
            show_count()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-3.")

if __name__ == "__main__":
    main()
