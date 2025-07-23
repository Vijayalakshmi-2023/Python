# Attendee class
class Attendee:
    total_attendees = 0  # Class variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Attendee.total_attendees += 1

    @classmethod
    def get_total_attendees(cls):
        return cls.total_attendees

    def __str__(self):
        return f"{self.name} ({self.email})"

# Session class
class Session:
    def __init__(self, title, speaker, time):
        self.title = title
        self.speaker = speaker
        self.time = time

    def __str__(self):
        return f"Session: {self.title}, Speaker: {self.speaker}, Time: {self.time}"

# Event class (aggregation: has many sessions)
class Event:
    def __init__(self, name):
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def list_sessions(self):
        for s in self.sessions:
            print(s)

# Registration class (aggregates attendee & sessions)
class Registration:
    def __init__(self, attendee, event):
        self.attendee = attendee
        self.event = event
        self.selected_sessions = []

    def assign_session(self, session):
        if session in self.event.sessions:
            self.selected_sessions.append(session)

    def show_registration(self):
        print(f"\n🧾 Registration for: {self.attendee}")
        print(f"🎤 Event: {self.event.name}")
        print("📚 Sessions:")
        for s in self.selected_sessions:
            print(f"   • {s.title} by {s.speaker} at {s.time}")

# Create an event
conf = Event("AI Conference 2025")

# Add sessions
conf.add_session(Session("Future of AI", "Dr. Smith", "10:00 AM"))
conf.add_session(Session("Ethics in AI", "Dr. Ada", "11:30 AM"))

# Create attendees
a1 = Attendee("Alice", "alice@example.com")
a2 = Attendee("Bob", "bob@example.com")

# Register attendees
reg1 = Registration(a1, conf)
reg1.assign_session(conf.sessions[0])
reg1.assign_session(conf.sessions[1])
reg1.show_registration()

reg2 = Registration(a2, conf)
reg2.assign_session(conf.sessions[1])
reg2.show_registration()

# View total attendees
print(f"\n👥 Total Attendees: {Attendee.get_total_attendees()}")
