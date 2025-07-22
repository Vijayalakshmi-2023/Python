# discounts.py

def flat_discount(total):
    """10% off if total > 1000"""
    if total > 1000:
        return total * 0.9
    return total
