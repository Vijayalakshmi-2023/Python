# calendar_view.py

def display_event(event):
    date, time = event["id"]
    desc = event["desc"]
    participants = ", ".join(event["participants"])
    return f"{date} {time} - {desc} (Participants: {participants})"

def display_events_for_date(events, date):
    filtered = [e for e in events if e["id"][0] == date]
    if not filtered:
        print(f"No events found for {date}.")
    else:
        print(f"\n📅 Events on {date}:")
        for event in filtered:
            print(display_event(event))

def display_all_event_dates(event_dates):
    print("\n🗓️ Dates with Events:")
    for d in sorted(event_dates):
        print(f"- {d}")
