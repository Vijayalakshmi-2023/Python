number = int(input("Enter a number to generate its multiplication table: "))
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
else:
    print("✅ Table completed.")
