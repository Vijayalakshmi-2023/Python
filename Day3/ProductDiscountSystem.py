product_name = input("Enter product name: ")
price = float(input("Enter product price (₹): "))
discount_percent = float(input("Enter discount percentage (%): "))
discount_amount = (discount_percent / 100) * price
price -= discount_amount  
print("\n🛍️ Discount Summary")
print("----------------------------")
print(f"Product       : {product_name}")
print(f"Discount      : {discount_percent}%")
print(f"Discount Amt  : ₹{discount_amount:.2f}")
print(f"Final Price   : ₹{price:.2f}")
