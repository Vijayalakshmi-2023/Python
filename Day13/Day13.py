##Section 1: Classes and Objects (1–10)
#Task 1: Car Class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Car: {self.brand} {self.model}, Price: ₹{self.price}")

# Instantiate two cars
car1 = Car("Toyota", "Camry", 3000000)
car2 = Car("Honda", "City", 1500000)

car1.display()
car2.display()


#Task 2:Bank Account Class
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Balance: ₹{self.balance}")

# Example usage
account = BankAccount("Amit")
account.deposit(5000)
account.withdraw(2000)
account.check_balance()


#Task 3: Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Example usage
student = Student("Ravi", 17, "A")
print(f"Student: {student.name}, Age: {student.age}, Grade: {student.grade}")


#Task 4: Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())


#Task 5: Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book: '{self.title}' by {self.author}")

# Example usage
book = Book("Wings of Fire", "A.P.J. Abdul Kalam")
book.display_info()


#Task 6:Laptop Class
class Laptop:
    warranty_period = 2  # shared across all instances (in years)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Example usage
laptop1 = Laptop("Dell", "Inspiron")
laptop2 = Laptop("HP", "Pavilion")
print(laptop1.warranty_period)
print(laptop2.warranty_period)


#Task 7: Movie Class
class Movie:
    total_movies = 0  # class variable

    def __init__(self, title):
        self.title = title
        Movie.total_movies += 1

# Example usage
m1 = Movie("Interstellar")
m2 = Movie("Inception")
print("Total movies created:", Movie.total_movies)


#Task 8: Product Class
class Product:
    company_name = "SuperMart"  # class variable shared
    def __init__(self, name, price):
        self.name = name       # instance variable
        self.price = price     # instance variable

# Example usage
p1 = Product("Soap", 30)
p2 = Product("Shampoo", 120)
print(f"{p1.name} from {p1.company_name} costs ₹{p1.price}")
print(f"{p2.name} from {p2.company_name} costs ₹{p2.price}")


#Task 9: Employee class
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self):
        return f"Employee[ID={self.id}, Name={self.name}, Salary=₹{self.salary}]"

# Example usage
emp = Employee("Kiran", 102, 55000)
print(emp)


#Task 10: Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

# Example usage
r1 = Rectangle(10, 5)
r2 = Rectangle(10, 5)
r3 = Rectangle(7, 3)

print("r1 == r2:", r1 == r2)
print("r1 == r3:", r1 == r3)


##Section 2: Inheritance (11–20)
#Task 11:
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

class Truck(Vehicle):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity

# Example
car = Car("Toyota", 180, 4)
print(car.brand, car.speed, car.doors)

#Task 12:
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' is created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent class constructor
        self.breed = breed
        print(f"Dog of breed '{self.breed}' is created")

# Create object
d = Dog("Tommy", "Labrador")


#Task 13:
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example
sq = Square(4)
tri = Triangle(3, 6)
print("Square area:", sq.area())
print("Triangle area:", tri.area())


#Task 14:
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

# Example
mgr = Manager("Rita", 101, "HR")
print(mgr.name, mgr.emp_id, mgr.department)


#Task 15:
class Father:
    def skills(self):
        print("Father: Driving, Carpentry")

class Mother:
    def skills(self):
        print("Mother: Cooking, Gardening")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Child: Painting")

# Example
c = Child()
c.skills()  # Method resolution follows MRO (Father first)

#Task 16:
class Teacher:
    def teach(self):
        print("Teaching subject...")

class MathTeacher(Teacher):
    def teach_math(self):
        print("Teaching Mathematics")

class ScienceTeacher(Teacher):
    def teach_science(self):
        print("Teaching Science")

# Example
math = MathTeacher()
sci = ScienceTeacher()
math.teach()
math.teach_math()
sci.teach_science()

#Task 17:
print(isinstance(math, MathTeacher))       # True
print(isinstance(math, Teacher))           # True
print(isinstance(math, ScienceTeacher))    # False

#Task 18:
print(issubclass(MathTeacher, Teacher))     # True
print(issubclass(Teacher, MathTeacher))     # False
print(issubclass(Child, Father))            # True

#Task 19:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, ram):
        super().__init__(name, price, brand)
        self.ram = ram

# Example
mobile = MobilePhone("iPhone", 80000, "Apple", "8GB")
print(mobile.name, mobile.price, mobile.brand, mobile.ram)

#Task 20:
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # MRO: D → B → C → A
    pass

d = D()
d.greet()  # Output: Hello from B

# View MRO
print(D.__mro__)


##Section 3: Encapsulation (21–25)
#Task 21:
class Student:
    def __init__(self, name, marks):
        self._name = name         # private by convention
        self._marks = marks       # private by convention

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks. Must be 0–100.")

# Example
s = Student("Anil", 85)
print(s.get_name(), s.get_marks())
s.set_marks(110)  # Invalid

#Task 22:
class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0        # private with double underscore

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

# Example
acc = BankAccount("Ravi")
acc.deposit(1000)
acc.withdraw(300)
print("Balance:", acc.get_balance())

#Task 23:
import re

class UserProfile:
    def __init__(self):
        self.__email = ""
        self.__phone = ""

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("Invalid email format.")

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        if re.fullmatch(r"\d{10}", phone):
            self.__phone = phone
        else:
            print("Phone must be 10 digits.")

    def get_phone(self):
        return self.__phone

# Example
user = UserProfile()
user.set_email("user@example.com")
user.set_phone("9876543210")
print(user.get_email(), user.get_phone())

#Task 24:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

# Example
emp = Employee("Meena", 40000)
print("Salary:", emp.get_salary())
emp.set_salary(-5000)  # Invalid


#Task 25:
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            if len(str(new_pin)) == 4:
                self.__pin = new_pin
                print("PIN changed successfully.")
            else:
                print("New PIN must be 4 digits.")
        else:
            print("Incorrect old PIN.")

# Example
locker = Locker(1234)
locker.change_pin(1234, 5678)  # Success
locker.change_pin(1111, 9999)  # Incorrect old PIN

##Section 4: Abstraction (26–30)
#Task 26:
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Example
payment = CreditCardPayment()
payment.pay(1500)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Example
payment = CreditCardPayment()
payment.pay(1500)

#Task 27:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Example
circle = Circle(5)
circle.describe()
print("Area:", circle.area())


#Task 28:
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example
d = Dog()
c = Cat()
print("Dog says:", d.speak())
print("Cat says:", c.speak())


#Task 29:
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# Example
car = Car()
car.start_engine()
car.stop_engine()


#Task 30:
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge uses 150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine uses 500W"

# Example
f = Fridge()
w = WashingMachine()
print(f.power_consumption())
print(w.power_consumption())


##Section 5: Polymorphism (31–35)
#Task 31:
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Example
a = Animal()
d = Dog()
a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks


#Task 32:
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

def render(shape):
    shape.draw()

# Example
c = Circle()
s = Square()
render(c)
render(s)

#Task 33:
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example
calc = Calculator()
print(calc.add(5))           # 5
print(calc.add(5, 10))       # 15
print(calc.add(5, 10, 20))   # 35

#Task 34:
class Sum:
    def add(self, *args):
        return sum(args)

# Example
s = Sum()
print(s.add(10, 20))             # 30
print(s.add(5, 10, 15))          # 30
print(s.add(1, 2, 3, 4, 5))      # 15

#Task 35:
class Notification:
    def send(self, msg):
        print("Sending notification:", msg)

class SMS(Notification):
    def send(self, msg):
        print("SMS sent:", msg)

class Email(Notification):
    def send(self, msg):
        print("Email sent:", msg)

class PushNotification(Notification):
    def send(self, msg):
        print("Push notification sent:", msg)

# Example
def notify_user(service: Notification, message: str):
    service.send(message)

notify_user(SMS(), "Your OTP is 1234")
notify_user(Email(), "Welcome to our service!")
notify_user(PushNotification(), "New update available.")

##Section 6: Magic (Dunder) Methods (36–40)
#Task 36:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print("Result:", v3)  # Output: (6, 8)


#Task 37:
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

# Example
p = Playlist(["Song1", "Song2", "Song3"])
print("Number of songs:", len(p))


#Task 38:
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, quantity):
        self.items[item] = quantity

# Example
cart = ShoppingCart()
cart["apple"] = 3
cart["banana"] = 5
print("Apples in cart:", cart["apple"])
print("Bananas in cart:", cart["banana"])


#Task 39:
class Inventory:
    def __init__(self):
        self.stock = ["apple", "banana", "orange"]

    def __contains__(self, item):
        return item in self.stock

# Example
inv = Inventory()
print("banana" in inv)   # True
print("grape" in inv)    # False


#Task 40:
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

# Example
m1 = Money(500)
m2 = Money(750)

print(m1 == m2)  # False
print(m1 > m2)   # False
print(m1 < m2)   # True


##Section 7: Composition & Aggregation (41–45)
#Task 41:
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # Engine created inside Car

    def show(self):
        print(f"Car: {self.brand}, Engine: {self.engine.horsepower} HP")

# Example
c = Car("BMW", 300)
c.show()


#Task 42:
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books  # List of existing Book objects

    def display_books(self):
        print(f"{self.name} Library has:")
        for book in self.books:
            print(f"- {book.title}")

# Example
b1 = Book("Python Basics")
b2 = Book("Data Structures")
lib = Library("City Central", [b1, b2])
lib.display_books()


#Task 43:
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = [
            Department("Computer Science"),
            Department("Physics"),
            Department("Mathematics")
        ]

    def show_departments(self):
        print(f"{self.name} University Departments:")
        for d in self.departments:
            print(f"- {d.name}")

# Example
u = University("Tech University")
u.show_departments()


#Task 44:
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees  # Accepts external Employee objects

    def list_employees(self):
        print(f"{self.name} Employees:")
        for emp in self.employees:
            print(f"- {emp.name}")

# Example
e1 = Employee("Anil")
e2 = Employee("Sita")
comp = Company("TechCorp", [e1, e2])
comp.list_employees()


#Task 45:
class Pilot:
    def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number
        self.pilot = Pilot("Captain Raj")
        self.crew = [CabinCrew("Neha"), CabinCrew("Karan")]
        self.passengers = [Passenger("Amit"), Passenger("Priya")]

    def flight_info(self):
        print(f"Flight: {self.flight_number}")
        print(f"Pilot: {self.pilot.name}")
        print("Cabin Crew:")
        for c in self.crew:
            print(f"- {c.name}")
        print("Passengers:")
        for p in self.passengers:
            print(f"- {p.name}")

# Example
f = Flight("AI-202")
f.flight_info()


##Section 8: Real-World Applications (46–50)
#Task 46:
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Account:
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}"
        return "Insufficient funds"

class Transaction:
    def __init__(self, account):
        self.account = account

    def perform(self, type, amount):
        if type == "deposit":
            return self.account.deposit(amount)
        elif type == "withdraw":
            return self.account.withdraw(amount)
        else:
            return "Invalid transaction type"

# Example
cust = Customer("Ravi", 101)
acc = Account(cust, 5000)
txn = Transaction(acc)
print(txn.perform("deposit", 2000))
print(txn.perform("withdraw", 1000))
print("Balance:", acc.balance)


#Task 47:
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index

    def is_correct(self, choice):
        return choice == self.correct_index

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for i, q in enumerate(self.questions):
            print(f"Q{i+1}: {q.text}")
            for idx, opt in enumerate(q.options):
                print(f"{idx}. {opt}")
            answer = int(input("Enter your choice: "))
            if q.is_correct(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Wrong.")
        print(f"Your score: {self.score}/{len(self.questions)}")

# Example (Use only in terminal)
# q1 = Question("Capital of India?", ["Mumbai", "Delhi", "Chennai"], 1)
# q2 = Question("2 + 2 = ?", ["3", "4", "5"], 1)
# quiz = Quiz([q1, q2])
# quiz.start()


#Task 48:
class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_booked = False

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Booking(Room):
    def __init__(self, room_number, price, customer):
        super().__init__(room_number, price)
        self.customer = customer
        self.is_booked = True

    def display(self):
        print(f"Room {self.room_number} booked by {self.customer.name} for ₹{self.price}")

# Example
cust = Customer("Amit", "9876543210")
booking = Booking(101, 2500, cust)
booking.display()


#Task 49:
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Student(Person):
    def get_role(self):
        return "Student"

class Teacher(Person):
    def get_role(self):
        return "Teacher"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def enroll(self, student):
        self.students.append(student)

class Grade:
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = score

# Example
t = Teacher("Ms. Rita")
s = Student("Manoj")
course = Course("Math", t)
course.enroll(s)
grade = Grade(s, course, 90)
print(f"{s.name} got {grade.score} in {course.name} taught by {t.name}")


#Task 50:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"You borrowed '{title}'"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"Returned '{title}'"
        return "Book not recognized or not borrowed"

    def search_book(self, keyword):
        found = [book.title for book in self.books if keyword.lower() in book.title.lower()]
        return found or "No books found"

# Example
lib = Library()
lib.add_book(Book("Python Crash Course", "Eric Matthes"))
lib.add_book(Book("Think Python", "Allen B. Downey"))
print(lib.borrow_book("Think Python"))
print(lib.return_book("Think Python"))
print(lib.search_book("Python"))
