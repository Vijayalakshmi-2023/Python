def track_expenses(*args):
    expenses = list(args)  # Store expenses in a list
    total = sum(expenses)  # Calculate total without GST

    # Apply 18% GST to each expense using map()
    apply_gst = lambda x: round(x * 1.18, 2)
    expenses_with_gst = list(map(apply_gst, expenses))
    total_with_gst = sum(expenses_with_gst)

    return expenses, total, expenses_with_gst, total_with_gst

# --- Example Usage ---
raw_expenses, subtotal, gst_expenses, grand_total = track_expenses(120, 250.5, 89.99, 300)

print("Original Expenses:", raw_expenses)
print("Subtotal (no GST): ₹", subtotal)

print("Expenses with GST (18%):", gst_expenses)
print("Total with GST: ₹", grand_total)
