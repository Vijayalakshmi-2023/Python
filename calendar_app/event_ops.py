# event_ops.py

def add_event(events, date, time, desc, participants):
    event_id = (date, time)  # immutable
    event = {
        "id": event_id,
        "desc": desc,
        "participants": set(participants)
    }
    events.append(event)

def delete_event(events, date, time):
    event_id = (date, time)
    for i, event in enumerate(events):
        if event["id"] == event_id:
            del events[i]
            return True
    return False

def update_event(events, date, time, desc=None, participants=None):
    event_id = (date, time)
    for event in events:
        if event["id"] == event_id:
            if desc:
                event["desc"] = desc
            if participants:
                event["participants"] = set(participants)
            return True
    return False

def get_all_event_dates(events):
    return {event["id"][0] for event in events}

def get_events_by_date(events, date):
    return [event for event in events if event["id"][0] == date]
