from abc import ABC, abstractmethod

# -------------------------
# Base Class: Vehicle
# -------------------------
class Vehicle(ABC):
    def __init__(self, reg_no, brand, daily_rate):
        self.reg_no = reg_no
        self.brand = brand
        self.daily_rate = daily_rate
        self.is_available = True

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def __str__(self):
        return f"{self.brand} ({self.reg_no}) - Rate: ₹{self.daily_rate}/day"

# -------------------------
# Derived Class: Bike
# -------------------------
class Bike(Vehicle):
    def calculate_rent(self, days):
        return days * self.daily_rate

# -------------------------
# Derived Class: Car
# -------------------------
class Car(Vehicle):
    def calculate_rent(self, days):
        insurance_fee = 100
        return days * self.daily_rate + insurance_fee

# -------------------------
# Customer Class
# -------------------------
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.rented_vehicle = None

    def __str__(self):
        return f"{self.name} ({self.contact})"

# -------------------------
# Rental System Class
# -------------------------
class Rental:
    total_vehicles_rented = 0

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def list_available(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles:
            if v.is_available:
                print(v)

    def rent_vehicle(self, customer, reg_no, days):
        for v in self.vehicles:
            if v.reg_no == reg_no and v.is_available:
                cost = v.calculate_rent(days)
                v.is_available = False
                customer.rented_vehicle = v
                Rental.total_vehicles_rented += 1
                print(f"\n{customer.name} rented {v.brand} for {days} days. Total: ₹{cost}")
                return
        print("Vehicle not available.")

    def return_vehicle(self, customer):
        v = customer.rented_vehicle
        if v:
            v.is_available = True
            print(f"\n{customer.name} returned {v.brand}. Thank you!")
            customer.rented_vehicle = None
        else:
            print("No vehicle to return.")

    @classmethod
    def get_total_rentals(cls):
        return cls.total_vehicles_rented

    @staticmethod
    def calculate_tax(amount):
        return round(amount * 0.18, 2)  # 18% GST


# Setup
rental = Rental()
rental.add_vehicle(Bike("B101", "Honda Activa", 150))
rental.add_vehicle(Car("C202", "Hyundai i20", 800))

# Customer
cust = Customer("Ravi", "9876543210")

# Show available vehicles
rental.list_available()

# Rent a vehicle
rental.rent_vehicle(cust, "C202", 3)

# Calculate tax separately
amount = cust.rented_vehicle.calculate_rent(3)
print("GST:", Rental.calculate_tax(amount))

# Return vehicle
rental.return_vehicle(cust)

# Total rentals
print("Total Rentals:", Rental.get_total_rentals())
