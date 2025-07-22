# scheduler.py

appointments = {}  # dict: date (str) → list of (time, person, purpose)

def add_appointment(date, time, person, purpose):
    entry = (time, person, purpose)
    appointments.setdefault(date, []).append(entry)

def remove_appointment(date, time, person):
    if date in appointments:
        appointments[date] = [
            appt for appt in appointments[date]
            if not (appt[0] == time and appt[1] == person)
        ]

def edit_appointment(date, time, person, new_time=None, new_person=None, new_purpose=None):
    if date in appointments:
        for i, (t, p, purp) in enumerate(appointments[date]):
            if t == time and p == person:
                updated = (
                    new_time or t,
                    new_person or p,
                    new_purpose or purp
                )
                appointments[date][i] = updated
                return True
    return False

def get_schedule():
    return dict(sorted(appointments.items()))

def get_unique_people():
    return {person for appts in appointments.values() for (_, person, _) in appts}
