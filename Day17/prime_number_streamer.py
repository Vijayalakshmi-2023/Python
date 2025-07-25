def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def prime_streamer(limit):
    yield 2  # First prime
    num = 3
    while num <= limit:
        if is_prime(num):
            yield num
        num += 2  # Skip even numbers
    return  # Ends with StopIteration
for prime in prime_streamer(50):
    print(prime, end=' ')
