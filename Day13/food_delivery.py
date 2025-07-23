# ----------------------
# Base User and Customer
# ----------------------
class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
# ----------------------
# Restaurant Class
# ----------------------
class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu  # dict: item → price
# ----------------------
# Delivery with Polymorphism
# ----------------------
class Delivery:
    def deliver(self, order):
        raise NotImplementedError

class BikeDelivery(Delivery):
    def deliver(self, order):
        print(f"Delivering '{order.item}' to {order.customer.address} via bike.")

class DroneDelivery(Delivery):
    def deliver(self, order):
        print(f"Delivering '{order.item}' to {order.customer.address} via drone.")
# ----------------------
# Order with Aggregation
# ----------------------
class Order:
    def __init__(self, customer, restaurant, item, delivery_method):
        self.customer = customer
        self.restaurant = restaurant  # Aggregated
        self.item = item
        self.delivery_method = delivery_method

    def place_order(self):
        if self.item in self.restaurant.menu:
            price = self.restaurant.menu[self.item]
            print(f"Order placed for '{self.item}' (₹{price}) from {self.restaurant.name}")
            self.delivery_method.deliver(self)
        else:
            print(f"Item '{self.item}' not available at {self.restaurant.name}")
# Setup
rest = Restaurant("Tasty Treats", {"Pizza": 300, "Burger": 150})
cust = Customer("Anil", "22 Main Street")

# Delivery method
delivery = BikeDelivery()

# Order
order = Order(cust, rest, "Pizza", delivery)
order.place_order()
