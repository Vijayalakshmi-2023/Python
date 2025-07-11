grocery_list = []

def add_item(item):
    grocery_list.append(item)
    print(f"Added '{item}' to the grocery list.")

def view_list():
    if grocery_list:
        print("Grocery List:")
        for i, item in enumerate(grocery_list, 1):
            print(f"{i}. {item}")
    else:
        print("Your grocery list is empty.")

def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"Removed '{item}' from the grocery list.")
    else:
        print(f"'{item}' is not in the grocery list.")

def main():
    while True:
        print("\nGrocery List Menu:")
        print("1. Add Item")
        print("2. View List")
        print("3. Remove Item")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            view_list()
        elif choice == '3':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
