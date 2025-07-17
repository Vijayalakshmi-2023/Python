# Duplicate SKU Checker for Inventory

# List of product SKUs with some duplicates
sku_list = [
    "SKU123", "SKU456", "SKU789", "SKU123", "SKU456", "SKU101", "SKU102"
]

# Convert list to set to remove duplicates
unique_skus = set(sku_list)

# Check if there are duplicates by comparing lengths
if len(sku_list) != len(unique_skus):
    print("Duplicates detected.")
else:
    print("No duplicates found.")

# Find and store duplicates
duplicates = set()
seen = set()

for sku in sku_list:
    if sku in seen:
        duplicates.add(sku)
    else:
        seen.add(sku)

print("Duplicate SKUs:", duplicates)
