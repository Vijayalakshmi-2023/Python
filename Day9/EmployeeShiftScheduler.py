from datetime import datetime

# Sample employee shifts, where each shift is represented as (employee_id, name, (start_time, end_time))
# Times are in the format "HH:MM" (24-hour format)
employee_shifts = [
    (101, "Anu", ("09:00", "17:00")),
    (102, "Banu", ("10:00", "18:00")),
    (103, "Charu", ("08:00", "16:00")),
    (104, "Deva", ("12:00", "20:00")),
    (105, "Elan", ("07:00", "15:00")),
    (106, "Govind", ("09:30", "17:30")),
    (107, "Hema", ("11:00", "19:00")),
]

# Function to calculate the total hours worked for a shift
def calculate_hours(start_time, end_time):
    # Convert time strings to datetime objects
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    
    # Calculate the difference in hours and minutes
    delta = end - start
    return delta.total_seconds() / 3600  # Convert seconds to hours

# 1. Access Specific Timings (nested indexing) and display shift details
def show_employee_shifts():
    print("Employee Shifts:")
    for employee in employee_shifts:
        employee_id, name, (start_time, end_time) = employee  # Unpacking tuple
        print(f"Employee ID: {employee_id}, Name: {name}, Shift: {start_time} to {end_time}")
    print("-" * 30)

# 2. Use slicing to show first 5 employees
def show_first_five_employees():
    print("First 5 Employees' Shifts:")
    first_five = employee_shifts[:5]  # Slicing the first 5 employees
    for employee in first_five:
        employee_id, name, (start_time, end_time) = employee  # Unpacking
        print(f"Employee ID: {employee_id}, Name: {name}, Shift: {start_time} to {end_time}")
    print("-" * 30)

# 3. Calculate payroll for each employee (assuming hourly rate of $20 per hour)
def calculate_payroll():
    hourly_rate = 20  # Hourly rate in dollars
    print("Payroll Calculation:")
    for employee in employee_shifts:
        employee_id, name, (start_time, end_time) = employee  # Unpacking tuple
        hours_worked = calculate_hours(start_time, end_time)  # Calculate hours worked
        payroll = hours_worked * hourly_rate  # Calculate payroll
        print(f"Employee ID: {employee_id}, Name: {name}, Hours Worked: {hours_worked:.2f} hours, Payroll: ${payroll:.2f}")
    print("-" * 30)

# Testing the functions
show_employee_shifts()  # Display all employee shifts
show_first_five_employees()  # Show first 5 employees
calculate_payroll()  # Calculate and show payroll for all employees
