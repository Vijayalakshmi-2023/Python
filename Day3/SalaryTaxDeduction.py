salary = float(input("Enter your base salary (in ₹): "))
tax = 0
if salary < 500000:
    tax = 0
elif salary <= 1000000:
    tax = 0.10 * salary  
else:
    tax = 0.20 * salary  

salary_after_tax = salary
salary_after_tax -= tax  

print("\n🧾 Salary Tax Report")
print("--------------------------")
print(f"Base Salary     : ₹{salary:,.2f}")
print(f"Tax Deducted    : ₹{tax:,.2f}")
print(f"Salary After Tax: ₹{salary_after_tax:,.2f}")
