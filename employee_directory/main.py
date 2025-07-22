# main.py

from directory.employee_ops import add_employee, remove_employee, update_employee
from search.search_ops import search_by_name, search_by_department
from utils.helpers import list_departments, format_employee

# Sample data
records = []
add_employee(records, 1001, "Alice", "HR", "Recruiter", "alice@example.com")
add_employee(records, 1002, "Bob", "Engineering", "Developer", "bob@corp.com")
add_employee(records, 1003, "Charlie", "Engineering", "DevOps", "charlie@corp.com")

# 🔍 Search
print("\n🔍 Employees in Engineering:")
for emp in search_by_department(records, "engineering"):
    print(format_employee(emp))

# 🔄 Update
print(update_employee(records, 1002, position="Senior Developer"))

# 🗑️ Remove
print(remove_employee(records, 1003))

# 📋 Departments
print("\n🏢 All Departments:")
print(list_departments(records))

# 🧾 Final Directory
print("\n📇 All Employees:")
for emp in records:
    print(format_employee(emp))
