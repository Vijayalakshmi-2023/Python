# Base Employee class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

# FullTimeEmployee class
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, daily_rate, working_days):
        super().__init__(emp_id, name)
        self.daily_rate = daily_rate
        self.working_days = working_days

    def calculate_salary(self):
        gross = self.daily_rate * self.working_days
        return Payroll.apply_tax(gross)

# PartTimeEmployee class
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        gross = self.hourly_rate * self.hours_worked
        return Payroll.apply_tax(gross)

# Payroll class with static method
class Payroll:
    @staticmethod
    def apply_tax(salary):
        tax = 0.10  # 10% tax
        return salary * (1 - tax)

    @staticmethod
    def generate_report(employee):
        print(f"\nPayroll for: {employee}")
        print(f"Net Salary: ₹{employee.calculate_salary():.2f}")

# Create employees
emp1 = FullTimeEmployee(emp_id=101, name="Alice", daily_rate=1000, working_days=22)
emp2 = PartTimeEmployee(emp_id=102, name="Bob", hourly_rate=200, hours_worked=80)

# Generate payroll
Payroll.generate_report(emp1)
Payroll.generate_report(emp2)
