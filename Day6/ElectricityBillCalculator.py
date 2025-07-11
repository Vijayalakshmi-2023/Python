def calculate_bill(*units):
    total_units = sum(units)

    # Slab rates (example):
    # 0-100 units: ₹1.5/unit
    # 101-200 units: ₹2.5/unit
    # 201-300 units: ₹4/unit
    # 301+ units: ₹6/unit

    if total_units <= 100:
        base_bill = total_units * 1.5
    elif total_units <= 200:
        base_bill = (100 * 1.5) + (total_units - 100) * 2.5
    elif total_units <= 300:
        base_bill = (100 * 1.5) + (100 * 2.5) + (total_units - 200) * 4
    else:
        base_bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (total_units - 300) * 6

    # Add 18% GST using lambda
    add_gst = lambda amount: amount + (amount * 0.18)
    total_bill = add_gst(base_bill)

    return round(total_bill, 2)

# --- Example usage ---
bill_amount = calculate_bill(120, 95, 80)  # Total: 295 units
print(f"Total electricity bill (incl. GST): ₹{bill_amount}")
