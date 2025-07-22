# validator.py

def validate_date(date_str):
    import re
    return bool(re.match(r"\d{4}-\d{2}-\d{2}$", date_str))

def validate_amount(amount_str):
    try:
        amt = float(amount_str)
        return amt > 0
    except:
        return False
