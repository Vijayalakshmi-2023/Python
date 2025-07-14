# Sample festival event schedule
event_schedule = [
    ("Opening Ceremony", ("09:00 AM", "10:00 AM", "Main Stage")),
    ("Music Performance", ("10:30 AM", "12:00 PM", "Outdoor Arena")),
    ("Art Exhibition", ("12:30 PM", "02:00 PM", "Art Gallery")),
    ("Food Tasting", ("02:30 PM", "04:00 PM", "Food Court")),
    ("Closing Party", ("06:00 PM", "08:00 PM", "Dance Hall"))
]

# 1. Display the full day's event schedule using index-based access
def display_schedule():
    print("Festival Event Schedule:")
    for i, (event_name, (start_time, end_time, location)) in enumerate(event_schedule, 1):
        print(f"Event {i}: {event_name}")
        print(f"  Time: {start_time} - {end_time}")
        print(f"  Location: {location}")
        print("-" * 30)

# 2. Access a specific event using index-based access
def access_event(index):
    if 1 <= index <= len(event_schedule):
        event_name, (start_time, end_time, location) = event_schedule[index - 1]  # Adjust for 0-based index
        print(f"Event {index}: {event_name}")
        print(f"  Time: {start_time} - {end_time}")
        print(f"  Location: {location}")
    else:
        print(f"Invalid event index {index}.")
    print("-" * 30)

# 3. Prevent accidental time edits using immutable tuples
def update_event_time(index, new_start_time, new_end_time):
    # Since tuples are immutable, we can't directly modify them, so we replace the tuple
    if 1 <= index <= len(event_schedule):
        event_name, (_, _, location) = event_schedule[index - 1]
        # Create new event details with updated times
        new_event = (event_name, (new_start_time, new_end_time, location))
        event_schedule[index - 1] = new_event  # Replace old event with new details
        print(f"Event {index} time updated to: {new_start_time} - {new_end_time}")
    else:
        print(f"Invalid event index {index}.")
    print("-" * 30)

# Testing the functions
display_schedule()  # Display all events
access_event(3)  # Access and display event 3 (Art Exhibition)
update_event_time(2, "11:00 AM", "12:30 PM")  # Update the Music Performance time
display_schedule()  # Display all events again after update
