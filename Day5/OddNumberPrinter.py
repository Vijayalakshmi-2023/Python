odd_numbers = []
i = 1

while i <= 20:
    if i % 2 == 0:
        i += 1
        continue  # Skip even numbers
    odd_numbers.append(i)
    i += 1

print("Odd numbers from 1 to 20:", odd_numbers)
