# Simple Discount Engine

# Step 1: Input product price
price = float(input("Enter product price: ₹"))

# Step 2: Apply discount based on price
if price >= 2000:
    discount = price * 0.20
elif price > 1000:
    discount = price * 0.10
else:
    discount = 0

# Step 3: Calculate final price
final_price = price - discount

# Step 4: Display summary
print("\n----- Discount Summary -----")
print(f"Original Price : ₹{price:.2f}")
print(f"Discount       : ₹{discount:.2f}")
print(f"Final Price    : ₹{final_price:.2f}")
print("-----------------------------")
