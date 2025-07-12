# To-Do List Manager
todo_list = []

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Show top 3 priority tasks")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks added yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter new task: ").strip()
    todo_list.append(task)
    print(f"Task '{task}' added.")

def complete_task():
    view_tasks()
    if todo_list:
        try:
            num = int(input("Enter the task number to mark as complete: "))
            if 1 <= num <= len(todo_list):
                completed = todo_list.pop(num - 1)
                print(f"✅ Task '{completed}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def show_top_priority():
    if todo_list:
        print("\nTop Priority Tasks:")
        for task in todo_list[:3]:  # Slicing top 3
            print("-", task)
    else:
        print("No tasks in the list.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        show_top_priority()
    elif choice == "5":
        print("Goodbye! Stay productive 💪")
        break
    else:
        print("Invalid option. Try again.")
