import math

history = []
memory = None

def evaluate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        history.append(f"{expr} = {result}")
        return result
    except Exception as e:
        return f"Error: {e}"

def unit_conversion():
    print("\n--- Unit Conversion ---")
    print("1. Length: meters <-> feet")
    print("2. Weight: kilograms <-> pounds")
    choice = input("Choose conversion type: ")

    try:
        value = float(input("Enter value to convert: "))
        if choice == '1':
            print("a. Meters to Feet")
            print("b. Feet to Meters")
            direction = input("Choose direction: ")
            if direction == 'a':
                print(f"{value} meters = {value * 3.28084:.4f} feet")
            elif direction == 'b':
                print(f"{value} feet = {value / 3.28084:.4f} meters")
            else:
                print("Invalid option.")
        elif choice == '2':
            print("a. Kilograms to Pounds")
            print("b. Pounds to Kilograms")
            direction = input("Choose direction: ")
            if direction == 'a':
                print(f"{value} kg = {value * 2.20462:.4f} lb")
            elif direction == 'b':
                print(f"{value} lb = {value / 2.20462:.4f} kg")
            else:
                print("Invalid option.")
        else:
            print("Invalid conversion type.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    global memory
    print("=== Simple Python Calculator ===")

    while True:
        print("\nOptions:")
        print("1. Calculate expression")
        print("2. Store result to memory")
        print("3. Recall memory")
        print("4. Clear memory")
        print("5. View history")
        print("6. Unit conversion")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            expr = input("Enter expression (supports + - * / % ** and parentheses): ")
            result = evaluate_expression(expr)
            print(f"Result: {result}")
        elif choice == '2':
            if history:
                memory = history[-1].split(' = ')[-1]
                print(f"Stored to memory: {memory}")
            else:
                print("No calculation yet.")
        elif choice == '3':
            print(f"Memory: {memory if memory else 'Empty'}")
        elif choice == '4':
            memory = None
            print("Memory cleared.")
        elif choice == '5':
            if history:
                print("\n--- Calculation History ---")
                for item in history:
                    print(item)
            else:
                print("No history available.")
        elif choice == '6':
            unit_conversion()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
