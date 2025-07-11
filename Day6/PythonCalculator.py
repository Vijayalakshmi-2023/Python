# Define operation functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"

# Calculator function that takes another function as an argument
def calculator(x, y, operation):
    return operation(x, y)

# --- Example Usage ---
print("Available operations: +  -  *  /")
op_symbol = input("Enter operation symbol: ").strip()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Choose operation dynamically
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

operation_func = operations.get(op_symbol)

if operation_func:
    result = calculator(a, b, operation_func)
    print(f"\nResult: {a} {op_symbol} {b} = {result}")
else:
    print("❌ Invalid operation selected.")
