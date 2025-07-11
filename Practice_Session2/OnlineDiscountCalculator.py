# Input: Price of the product
price = float(input("Enter the price of the product: ₹"))

# Variable to store discount
discount = 0

# Apply discount using if-elif-else
if price >= 2000:
    discount = price * 0.30  # 30% discount
elif price >= 1000:
    discount = price * 0.10  # 10% discount
else:
    discount = 0             # No discount

# Final price after discount
final_price = price - discount

# Output
print(f"Original Price: ₹{price:.2f}")
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Price to Pay: ₹{final_price:.2f}")
