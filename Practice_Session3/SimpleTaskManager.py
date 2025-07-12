# Simple Task Manager

# Task list: each task is a dict with 'name' and 'completed' status
tasks = []

# Function to add a new task
def add_task():
    task_name = input("Enter task name: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added.\n")
    else:
        print("Task name cannot be empty.\n")

# Function to delete a task
def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['name']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to mark a task as complete
def mark_complete():
    show_tasks()
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print(f"Task '{tasks[index]['name']}' marked as complete.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to display tasks
def show_tasks():
    print("\n=== Task List ===")
    if not tasks:
        print("No tasks available.\n")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['name']} [{status}]")
        print()

# Main menu loop
def main():
    while True:
        print("=== Task Manager ===")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task Complete")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Start the program
main()
