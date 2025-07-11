def add_employee(**kwargs):
    name = kwargs.get('name', 'Unknown')
    role = kwargs.get('role', 'Not specified')
    salary = kwargs.get('salary', 0)

    print(f"Added Employee: {name} | Role: {role} | Salary: ₹{salary}")

    return {
        "name": name,
        "role": role,
        "salary": salary
    }

# Dictionary to store all employees
employee_db = {}

# Adding employees
employee1 = add_employee(name="Alice", role="Manager", salary=80000)
employee2 = add_employee(name="Bob", role="Developer", salary=60000)

# Store in the dictionary with unique IDs
employee_db["E001"] = employee1
employee_db["E002"] = employee2

# --- Final Output ---
print("\nAll Employees:")
for emp_id, info in employee_db.items():
    print(f"{emp_id} -> {info}")
