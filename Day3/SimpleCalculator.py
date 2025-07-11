num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /, %, **): ").strip()
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
    else:
        print("❌ Error: Modulo by zero is not allowed.")
elif operation == "**":
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")
else:
    print("❌ Invalid operation. Please choose from +, -, *, /, %, **.")
