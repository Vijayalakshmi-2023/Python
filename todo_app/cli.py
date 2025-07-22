# cli.py

def display_task(task):
    title, due = task["task"]
    status = "✔️ Done" if task["completed"] else "🕒 Pending"
    tags = ", ".join(task["tags"])
    return (f"Title: {title}\nDue: {due} | Priority: {task['priority']} | Status: {status}\n"
            f"Tags: {tags}\nNotes: {task['notes']}\n")

def show_all_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        print(display_task(task))
        print("-" * 40)

def show_grouped_tasks(grouped):
    for priority, task_list in grouped.items():
        print(f"\n📌 Priority: {priority}")
        for task in task_list:
            print(display_task(task))
            print("-" * 30)
