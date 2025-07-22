# main.py

from task_ops import (
    add_task, complete_task, delete_task,
    show_overdue_tasks, group_by_priority
)
from cli import show_all_tasks, show_grouped_tasks

tasks = []

# Add tasks
add_task(tasks, "Submit report", "2025-07-20", "High", ["work", "urgent"], "Send it to manager")
add_task(tasks, "Buy groceries", "2025-07-25", "Low", ["personal"], "Milk, Bread, Eggs")
add_task(tasks, "Pay bills", "2025-07-21", "Medium", ["finance"], "Electricity & Internet")

# Mark one as completed
complete_task(tasks, "Pay bills")

# Delete a task
delete_task(tasks, "Buy groceries")

# Show all tasks
print("\n📋 All Tasks:")
show_all_tasks(tasks)

# Show overdue
print("\n⚠️ Overdue Tasks:")
overdue = show_overdue_tasks(tasks)
show_all_tasks(overdue)

# Group by priority
print("\n📂 Tasks Grouped by Priority:")
grouped = group_by_priority(tasks)
show_grouped_tasks(grouped)
