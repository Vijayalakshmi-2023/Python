import logging

# Configure logging
logging.basicConfig(filename="calculator_errors.log",
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class InvalidOperationError(Exception):
    pass

def smart_calculator():
    try:
        # Input
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))

        # Operation
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif op == '%':
            if num2 == 0:
                raise ZeroDivisionError("Cannot modulo by zero.")
            result = num1 % num2
        else:
            raise InvalidOperationError(f"Invalid operator '{op}'")

    except ValueError as ve:
        logging.error("ValueError occurred", exc_info=True)
        print("Input Error: Please enter valid numbers.")
    except ZeroDivisionError as zde:
        logging.error("ZeroDivisionError occurred", exc_info=True)
        print("Math Error:", zde)
    except InvalidOperationError as ioe:
        logging.error("InvalidOperationError occurred", exc_info=True)
        print("Operation Error:", ioe)
    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("Unexpected error:", e)
    else:
        print(f"Result: {num1} {op} {num2} = {result}")
    finally:
        print("Thank you for using Smart Calculator!")

# Run the calculator
smart_calculator()
