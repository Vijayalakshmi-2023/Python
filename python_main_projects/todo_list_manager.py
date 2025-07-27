import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Task Title: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    due_date = input("Due Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(due_date, '%Y-%m-%d')  # validate format
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    tasks.append({
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    print("Task added successfully.")

def view_tasks(tasks, sort_key=None):
    if not tasks:
        print("No tasks to show.")
        return

    if sort_key:
        if sort_key in ["priority", "due_date"]:
            tasks.sort(key=lambda x: x[sort_key])

    for idx, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{idx}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Completed: {status}")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in tasks if keyword in t['title'].lower()]
    if results:
        view_tasks(results)
    else:
        print("No matching tasks found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Sort by Priority")
        print("7. Sort by Due Date")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            search_tasks(tasks)
        elif choice == '6':
            view_tasks(tasks, sort_key="priority")
        elif choice == '7':
            view_tasks(tasks, sort_key="due_date")
        elif choice == '0':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
