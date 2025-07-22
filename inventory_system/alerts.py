# alerts.py

def restock_alerts(inventory, threshold=10):
    alerts = []
    for item, (qty, _) in inventory.items():
        if qty <= threshold:
            alerts.append(f"⚠️ Low stock for '{item}': only {qty} left.")
    return alerts
