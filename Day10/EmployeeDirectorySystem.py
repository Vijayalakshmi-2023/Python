employees = {}
# Add new employee (prevent overwriting existing record)
def add_employee(emp_id, name, dept, salary):
    employees.setdefault(emp_id, {"name": name, "dept": dept, "salary": salary})
    print(f"Employee {emp_id} added (if not already exists).")

# Update salary or department
def update_employee(emp_id, salary=None, dept=None):
    if emp_id in employees:
        if salary is not None:
            employees[emp_id]["salary"] = salary
        if dept is not None:
            employees[emp_id]["dept"] = dept
        print(f"Employee {emp_id} updated.")
    else:
        print(f"Employee {emp_id} not found.")

# Delete employee using pop()
def delete_employee(emp_id):
    removed = employees.pop(emp_id, None)
    if removed:
        print(f"Employee {emp_id} deleted.")
    else:
        print(f"Employee {emp_id} not found.")

# Search employees by department
def search_by_department(dept_name):
    print(f"\nEmployees in Department: {dept_name}")
    found = False
    for emp_id, info in employees.items():
        if info["dept"].lower() == dept_name.lower():
            print(f"  ID: {emp_id}, Name: {info['name']}, Salary: {info['salary']}")
            found = True
    if not found:
        print("  No employees found in this department.")

# Show all employees
def show_all_employees():
    print("\nAll Employees:")
    for emp_id, info in employees.items():
        print(f"  ID: {emp_id}, Name: {info['name']}, Dept: {info['dept']}, Salary: {info['salary']}")

# Add employees
add_employee(101, "Anu", "HR", 50000)
add_employee(102, "Banu", "IT", 65000)
add_employee(103, "Charu", "Finance", 60000)
add_employee(101, "New Name", "New Dept", 99999)  # Will not overwrite

# Update
update_employee(102, salary=70000)
update_employee(104, salary=80000)  # Non-existent

# Delete
delete_employee(103)
delete_employee(999)  # Non-existent

# Search by department
search_by_department("IT")
search_by_department("Marketing")

# Show all records
show_all_employees()
