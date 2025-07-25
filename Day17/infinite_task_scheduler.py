import itertools
import time
from datetime import datetime

def task_scheduler(tasks):
    # Infinite cycle through tasks
    for task in itertools.cycle(tasks):
        start_time = datetime.now()
        yield task, start_time  # Yield task with timestamp lazily
tasks = ["Backup", "Email Sync", "Disk Cleanup", "Security Scan"]
scheduler = task_scheduler(tasks)

for i in range(10):  # Stop after 10 iterations
    task, timestamp = next(scheduler)
    print(f"[{i+1}] Task: {task} (Scheduled at: {timestamp.strftime('%H:%M:%S')})")
