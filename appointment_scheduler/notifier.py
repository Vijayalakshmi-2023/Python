# notifier.py

from datetime import date
from scheduler import appointments

def show_today_appointments():
    today = date.today().isoformat()
    if today in appointments:
        print(f"📅 Appointments for today ({today}):")
        for time, person, purpose in appointments[today]:
            print(f"⏰ {time} - {person} ({purpose})")
    else:
        print("✅ No appointments today.")
