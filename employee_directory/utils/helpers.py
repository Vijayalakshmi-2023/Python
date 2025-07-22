# utils/helpers.py

def list_departments(records):
    return {rec["department"] for rec in records}

def format_employee(emp):
    emp_id, name = emp["id"]
    return f"{emp_id}: {name} | {emp['position']} in {emp['department']} | {emp['email']}"
