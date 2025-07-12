# Text-Based Calculator

# List to store past results
history = []

# Operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to show history
def show_history():
    if not history:
        print("No calculations yet.\n")
        return
    print("\n=== Calculation History ===")
    for i, result in enumerate(history, start=1):
        print(f"{i}. {result}")
    print()

# Function to perform calculation
def calculate():
    op = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    if op not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation. Try again.\n")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.\n")
        return

    if op == "add":
        result = add(num1, num2)
    elif op == "subtract":
        result = subtract(num1, num2)
    elif op == "multiply":
        result = multiply(num1, num2)
    elif op == "divide":
        result = divide(num1, num2)

    print(f"Result: {result}\n")
    history.append(f"{op.capitalize()} {num1} and {num2} = {result}")

# Main loop
def main():
    while True:
        print("=== Text-Based Calculator ===")
        print("1. Calculate")
        print("2. Show History")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculate()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the calculator
main()
