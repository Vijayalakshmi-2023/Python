# Class Schedule Collision Detector

# Slots are represented as time blocks, e.g., "Mon 9-10", "Tue 11-12"
# Schedule for Class A
class_a_slots = {"Mon 9-10", "Wed 11-12", "Fri 14-15"}

# Schedule for Class B
class_b_slots = {"Tue 10-11", "Wed 11-12", "Thu 13-14"}

# Find conflicting slots (common time blocks)
conflicts = class_a_slots.intersection(class_b_slots)
print("Conflicting class slots:", conflicts)

# Suggest available slots for Class B that don't conflict with Class A
available_slots = class_b_slots.difference(class_a_slots)
print("Available slots for Class B without conflict:", available_slots)

# If we want to add a new slot to Class A schedule
new_slot = "Thu 13-14"
class_a_slots.add(new_slot)
print("Updated Class A slots:", class_a_slots)
