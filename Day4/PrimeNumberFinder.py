# Prime Number Finder (1–50)

print("Prime numbers between 1 and 50:")

# Loop through numbers from 2 to 50
for num in range(2, 51):
    is_prime = True  # Assume number is prime

    # Check for divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Not prime
            break

    # If no divisors found, it's prime
    if is_prime:
        print(num, end=" ")
