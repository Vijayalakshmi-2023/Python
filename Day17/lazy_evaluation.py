def lazy_calculator(operations):
    return (
        a + b if op == '+' else
        a - b if op == '-' else
        a * b if op == '*' else
        a / b if op == '/' and b != 0 else
        'Invalid Operation'
        for a, b, op in operations
    )
# Input: list of (a, b, operation)
ops = [(10, 5, '+'), (10, 2, '/'), (7, 0, '/'), (4, 3, '*'), (9, 3, '-')]

lazy_results = lazy_calculator(ops)

# Yield result only when needed
print(next(lazy_results))  # 15
print(next(lazy_results))  # 5.0
print(next(lazy_results))  # Invalid Operation
print(next(lazy_results))  # 12
print(next(lazy_results))  # 6
