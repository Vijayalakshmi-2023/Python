# ---------------------
# Base Class: Device
# ---------------------
class Device:
    def __init__(self, name):
        self.name = name
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self._is_on = False
        print(f"{self.name} is now OFF.")

    def operate(self):
        raise NotImplementedError("Subclasses must implement operate()")

    def __str__(self):
        return f"{self.name} - {'ON' if self._is_on else 'OFF'}"

# ---------------------
# Subclass: Light
# ---------------------
class Light(Device):
    def operate(self):
        if not self._is_on:
            self.turn_on()
        else:
            self.turn_off()

# ---------------------
# Subclass: AC
# ---------------------
class AC(Device):
    def operate(self):
        if not self._is_on:
            self.turn_on()
            print("AC is cooling the room...")
        else:
            self.turn_off()
            print("AC stopped.")

# ---------------------
# Subclass: Fan
# ---------------------
class Fan(Device):
    def operate(self):
        if not self._is_on:
            self.turn_on()
            print("Fan is spinning...")
        else:
            self.turn_off()
            print("Fan stopped.")

# ---------------------
# SmartHub (Composition)
# ---------------------
class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"[+] Added device: {device.name}")

    def control_all(self):
        print("\nControlling all devices...")
        for device in self.devices:
            device.operate()

    def show_status(self):
        print("\nDevice Status:")
        for device in self.devices:
            print(device)

# Create devices
light1 = Light("Bedroom Light")
fan1 = Fan("Living Room Fan")
ac1 = AC("Bedroom AC")

# Create hub and add devices
hub = SmartHub()
hub.add_device(light1)
hub.add_device(fan1)
hub.add_device(ac1)

# Show current status
hub.show_status()

# Operate all devices (turn on)
hub.control_all()

# Operate all again (turn off)
hub.control_all()

# Final status
hub.show_status()
