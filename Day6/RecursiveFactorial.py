# Recursive function to calculate factorial
def factorial(n):
    if n < 0:
        return "Invalid input (factorial not defined for negative numbers)"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function to get nth Fibonacci number
def fibonacci(n):
    if n < 0:
        return "Invalid input (Fibonacci not defined for negative numbers)"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# --- Demo usage ---
num = 5

fact_result = factorial(num)
fib_result = fibonacci(num)

print(f"Factorial of {num} is: {fact_result}")
print(f"{num}th Fibonacci number is: {fib_result}")
