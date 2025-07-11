orders = []
while True:
    item = input("Enter a food item (type 'done' to finish): ").strip()

    if item.lower() == "done":
        break  # Exit when user is done

    if item == "":
        print("⚠️ Empty entry skipped.")
        continue  # Skip blank inputs

    orders.append(item)
    print(f"✅ '{item}' added to order.")
else:
    # This else block will not run because break is always used to exit
    print("Order entry completed.")

# Show final order summary
print("\n🧾 Order Summary:")
if orders:
    for i, item in enumerate(orders, 1):
        print(f"{i}. {item}")
    print(f"Total items ordered: {len(orders)}")
else:
    print("No items were ordered.")
