# Employee Management System
employees = [
    ["Alice", "Manager"],
    ["Bob", "Developer"],
    ["Charlie", "Designer"]
]

def show_menu():
    print("\n👔 Employee Management System")
    print("1. View all employees")
    print("2. Add new employee")
    print("3. Update employee details")
    print("4. Remove an employee")
    print("5. View employee by index")
    print("6. Sort employees alphabetically")
    print("7. Exit")

def view_employees():
    if not employees:
        print("No employees to show.")
    else:
        print("\n📋 Employee Records:")
        for name, position in employees:
            print(f"Name: {name}, Position: {position}")

def add_employee():
    name = input("Enter employee name: ").strip()
    position = input("Enter position: ").strip()
    employees.append([name, position])
    print(f"✅ Added {name} as {position}.")

def update_employee():
    view_employees()
    name = input("Enter the name of the employee to update: ").strip()
    for emp in employees:
        if emp[0].lower() == name.lower():
            new_name = input("Enter new name: ").strip()
            new_position = input("Enter new position: ").strip()
            emp[0] = new_name
            emp[1] = new_position
            print(f"🔄 Updated to {new_name}, {new_position}.")
            return
    print(f"❌ Employee '{name}' not found.")

def remove_employee():
    name = input("Enter the name of the employee to remove: ").strip()
    for emp in employees:
        if emp[0].lower() == name.lower():
            employees.remove(emp)
            print(f"🗑️ Removed {name}.")
            return
    print(f"❌ Employee '{name}' not found.")

def view_by_index():
    try:
        index = int(input("Enter index of employee (starting from 0): "))
        emp = employees[index]
        print(f"🔍 At index {index}: {emp[0]}, {emp[1]}")
    except IndexError:
        print("❌ Invalid index.")
    except ValueError:
        print("❌ Please enter a valid number.")

def sort_employees():
    employees.sort(key=lambda e: e[0].lower())
    print("✅ Employees sorted alphabetically by name.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–7): ")

    if choice == "1":
        view_employees()
    elif choice == "2":
        add_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        remove_employee()
    elif choice == "5":
        view_by_index()
    elif choice == "6":
        sort_employees()
    elif choice == "7":
        print("Exiting Employee Management System. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
