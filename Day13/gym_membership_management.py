# -------------------------------
# Base Member class
# -------------------------------
class Member:
    total_members = 0  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions = []
        Member.total_members += 1

    def register_sessions(self, *args):
        self.sessions.extend(args)
        print(f"{self.name} registered for sessions: {', '.join(args)}")

    def view_sessions(self):
        return self.sessions

    def __str__(self):
        return f"Member: {self.name}, Age: {self.age}, Sessions: {self.sessions}"

# -------------------------------
# Trainer class
# -------------------------------
class Trainer:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.assigned_members = []

    def assign_member(self, member):
        self.assigned_members.append(member.name)
        print(f"Trainer {self.name} assigned to {member.name}")

    def __str__(self):
        return f"Trainer: {self.name}, Specialty: {self.specialty}, Assigned: {self.assigned_members}"

# -------------------------------
# Schedule class
# -------------------------------
class Schedule:
    def __init__(self):
        self.bookings = {}  # key: time slot, value: member name

    def book_slot(self, member, slot):
        if slot not in self.bookings:
            self.bookings[slot] = member.name
            print(f"Slot '{slot}' booked for {member.name}")
        else:
            print(f"Slot '{slot}' is already booked by {self.bookings[slot]}")

    def show_bookings(self):
        return self.bookings

# -------------------------------
# Subscription class
# -------------------------------
class Subscription(Member):
    def __init__(self, name, age, plan_type):
        super().__init__(name, age)
        self.plan_type = plan_type

    def __str__(self):
        return f"{super().__str__()}, Plan: {self.plan_type}"

# Create trainer
t1 = Trainer("Raj", "Yoga")
t2 = Trainer("Meera", "Weight Training")

# Create members
m1 = Subscription("Alice", 28, "Monthly")
m2 = Subscription("Bob", 35, "Annual")

# Register for sessions
m1.register_sessions("Yoga", "Zumba")
m2.register_sessions("Weights", "Cardio", "Swimming")

# Assign trainers
t1.assign_member(m1)
t2.assign_member(m2)

# Book schedule
s = Schedule()
s.book_slot(m1, "7AM-8AM")
s.book_slot(m2, "7AM-8AM")  # Already booked
s.book_slot(m2, "8AM-9AM")

# View info
print("\n--- Summary ---")
print(m1)
print(m2)
print(t1)
print(t2)
print("Bookings:", s.show_bookings())
print("Total Members:", Member.total_members)
