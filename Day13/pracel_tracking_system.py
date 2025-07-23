class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.address}, Ph: {self.phone}"


class Sender(Person):
    pass


class Receiver(Person):
    pass

class Parcel:
    _id_counter = 1000  # Class variable to auto-generate ID

    def __init__(self, sender, receiver, weight, delivery_type):
        self.sender = sender                  # Composition
        self.receiver = receiver              # Composition
        self.weight = weight
        self.delivery_type = delivery_type
        self.tracking_id = self.generate_tracking_id()

    @classmethod
    def generate_tracking_id(cls):
        cls._id_counter += 1
        return f"PCL{cls._id_counter}"

    @staticmethod
    def validate_tracking_id(tracking_id):
        return tracking_id.startswith("PCL") and tracking_id[3:].isdigit()

    def __str__(self):
        return (f"Parcel ID: {self.tracking_id}\n"
                f"From: {self.sender}\n"
                f"To: {self.receiver}\n"
                f"Weight: {self.weight} kg | Type: {self.delivery_type}")

class Tracking:
    def __init__(self):
        self.status = {}

    def update_status(self, tracking_id, message):
        self.status[tracking_id] = message

    def get_status(self, tracking_id):
        return self.status.get(tracking_id, "❌ Tracking ID not found.")

# Create sender and receiver
sender = Sender("Alice", "123 Main St, Delhi", "9876543210")
receiver = Receiver("Bob", "45 Park Ave, Mumbai", "9123456780")

# Create a parcel
parcel = Parcel(sender, receiver, 2.5, "Express")

# Display parcel info
print(parcel)

# Use tracking
tracker = Tracking()
tracker.update_status(parcel.tracking_id, "Dispatched from Delhi Hub")
print("\n📦 Status Check:")
print(tracker.get_status(parcel.tracking_id))

# Validate tracking ID
print("\n🔍 ID Validation:")
print(f"{parcel.tracking_id} valid? {Parcel.validate_tracking_id(parcel.tracking_id)}")
print(f"ABC123 valid? {Parcel.validate_tracking_id('ABC123')}")
