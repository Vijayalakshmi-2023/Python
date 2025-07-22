# report_ops.py

from sale_ops import sales, products

def get_unique_buyers():
    return {buyer for (_, buyer, _, _) in sales}

def sales_report():
    report = {}
    for code, buyer, qty, time in sales:
        if code not in report:
            report[code] = {"qty": 0, "revenue": 0.0}
        price = products[code]["price"]
        revenue = price * qty
        report[code]["qty"] += qty
        report[code]["revenue"] += revenue

    return report

def print_report():
    print("🧾 Sales Report:")
    for code, data in sales_report().items():
        name = products[code]["name"]
        print(f"{code} - {name}: {data['qty']} sold, ₹{data['revenue']:.2f} revenue")
