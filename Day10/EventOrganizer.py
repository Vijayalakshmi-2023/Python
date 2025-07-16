# Structure: {event_name: {"participants": [...], "max": ...}}
events = {
    "Tech Conference": {"participants": ["Alice", "Bob"], "max": 100},
    "Music Concert": {"participants": ["Charlie", "David"], "max": 50},
    "Art Exhibition": {"participants": ["Eve"], "max": 30}
}

# Register a participant for an event
def register_participant(event_name, participant_name):
    if event_name in events:
        event = events[event_name]
        # Check if there is space for more participants
        if len(event["participants"]) < event["max"]:
            if participant_name not in event["participants"]:
                event["participants"].append(participant_name)
                print(f"{participant_name} has been registered for {event_name}.")
            else:
                print(f"{participant_name} is already registered for {event_name}.")
        else:
            print(f"Sorry, {event_name} is full. Cannot register more participants.")
    else:
        print(f"{event_name} does not exist.")

# Cancel a participant's registration
def cancel_registration(event_name, participant_name):
    if event_name in events:
        event = events[event_name]
        if participant_name in event["participants"]:
            event["participants"].remove(participant_name)
            print(f"{participant_name}'s registration has been cancelled for {event_name}.")
        else:
            print(f"{participant_name} is not registered for {event_name}.")
    else:
        print(f"{event_name} does not exist.")

# Count the number of participants in an event
def count_participants(event_name):
    if event_name in events:
        participants_count = len(events[event_name]["participants"])
        print(f"{event_name} has {participants_count} participants.")
    else:
        print(f"{event_name} does not exist.")

# Register new participants
register_participant("Tech Conference", "George")
register_participant("Music Concert", "Helen")
register_participant("Art Exhibition", "Frank")

# Try to register when the event is full
register_participant("Music Concert", "Ivy")

# Cancel a registration
cancel_registration("Tech Conference", "Bob")

# Count participants in each event
count_participants("Tech Conference")
count_participants("Music Concert")
count_participants("Art Exhibition")
