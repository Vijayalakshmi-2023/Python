num = 1

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue  # Skip even numbers

    print(f"Number: {num}, Square: {num ** 2}")
    num += 1
