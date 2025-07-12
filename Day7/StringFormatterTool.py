# Input from user
name = input("Enter your name: ").strip()
salary_input = input("Enter your salary (e.g., 50000.456): ").strip()

# Modify name using .title()
formatted_name = name.title()

# Clean and convert salary input (e.g., if someone writes "50,000.00")
clean_salary_str = salary_input.replace(",", "")
salary = float(clean_salary_str)

# Format using % formatting
output = "My name is %s and I earn ₹%.2f" % (formatted_name, salary)

# Final output
print("\nFormatted Output:")
print(output)
