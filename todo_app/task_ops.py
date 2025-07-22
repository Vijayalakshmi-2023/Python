# task_ops.py

from datetime import date

def add_task(tasks, title, due_date, priority, tags, notes):
    task = {
        "task": (title, due_date),  # Immutable info
        "priority": priority,
        "tags": set(tags),
        "notes": notes,
        "completed": False
    }
    tasks.append(task)

def complete_task(tasks, title):
    for task in tasks:
        if task["task"][0] == title:
            task["completed"] = True
            return True
    return False

def delete_task(tasks, title):
    for i, task in enumerate(tasks):
        if task["task"][0] == title:
            tasks.pop(i)
            return True
    return False

def show_overdue_tasks(tasks):
    today = date.today().isoformat()
    return [task for task in tasks if task["task"][1] < today and not task["completed"]]

def group_by_priority(tasks):
    grouped = {}
    for task in tasks:
        key = task["priority"]
        grouped.setdefault(key, []).append(task)
    return grouped
