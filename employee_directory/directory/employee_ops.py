# directory/employee_ops.py

def add_employee(records, emp_id, name, department, position, email):
    emp = {
        "id": (emp_id, name),
        "department": department,
        "position": position,
        "email": email
    }
    records.append(emp)
    return f"✅ Added: {name} ({emp_id})"

def remove_employee(records, emp_id):
    for i, rec in enumerate(records):
        if rec["id"][0] == emp_id:
            del records[i]
            return f"🗑️ Removed employee {emp_id}"
    return "❌ Employee not found."

def update_employee(records, emp_id, **kwargs):
    for rec in records:
        if rec["id"][0] == emp_id:
            rec.update(kwargs)
            return f"🔄 Updated employee {emp_id}"
    return "❌ Employee not found."
