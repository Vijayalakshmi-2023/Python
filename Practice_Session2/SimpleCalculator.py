# Input: Two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter operation (+, -, *, /): ")

# Perform calculation using if-elif-else
if op == '+':
    result = num1 + num2
    print(f"✅ Result: {num1} + {num2} = {result}")
elif op == '-':
    result = num1 - num2
    print(f"✅ Result: {num1} - {num2} = {result}")
elif op == '*':
    result = num1 * num2
    print(f"✅ Result: {num1} * {num2} = {result}")
elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"✅ Result: {num1} / {num2} = {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
else:
    print("❌ Error: Invalid operator. Please use +, -, *, or /.")
