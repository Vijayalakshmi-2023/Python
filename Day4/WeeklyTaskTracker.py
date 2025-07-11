# Weekly Task Tracker

# Predefined list of tasks
tasks = ["Submit report", "Team meeting", "Code review", "Write documentation", "Test features", "Plan next sprint", "Rest day"]

# Days of the week starting from Monday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Use enumerate to display each day's task
for index, task in enumerate(tasks):
    print(f"{days[index]}: {task}")
