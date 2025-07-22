# main.py

from event_ops import (
    add_event, delete_event, update_event,
    get_all_event_dates, get_events_by_date
)
from calendar_view import (
    display_event, display_events_for_date, display_all_event_dates
)

# In-memory event list
events = []

# Add events
add_event(events, "2025-07-25", "10:00", "Team Meeting", ["Alice", "Bob"])
add_event(events, "2025-07-25", "15:00", "Doctor Appointment", ["Charlie"])
add_event(events, "2025-07-26", "09:00", "Yoga Class", ["Alice", "Daisy"])

# Update an event
update_event(events, "2025-07-25", "10:00", desc="Project Sync-Up")

# Delete an event
delete_event(events, "2025-07-25", "15:00")

# Show dates with events
event_dates = get_all_event_dates(events)
display_all_event_dates(event_dates)

# Show events for a specific date
display_events_for_date(events, "2025-07-25")
display_events_for_date(events, "2025-07-26")
