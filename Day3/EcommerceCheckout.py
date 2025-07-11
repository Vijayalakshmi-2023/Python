valid_discounts = {
    "SAVE10": 10,   # 10% off
    "SAVE20": 20,   # 20% off
    "FREESHIP": 5   # 5% off as token
}

price = float(input("Enter product price (₹): "))
quantity = int(input("Enter quantity: "))
code = input("Enter discount code (or press Enter to skip): ").strip().upper()

total = price * quantity

if code in valid_discounts:
    discount_percent = valid_discounts[code]
    discount_amount = (discount_percent / 100) * total
    total -= discount_amount 
    print(f"\n✅ Discount code '{code}' applied: {discount_percent}% off (₹{discount_amount:.2f})")
else:
    discount_amount = 0
    if code != "":
        print(f"\n❌ Invalid discount code '{code}'. No discount applied.")


print(f"🛒 Total after discount: ₹{total:.2f}")
