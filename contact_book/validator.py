# validator.py

import re

def validate_name(name):
    return isinstance(name, str) and len(name.strip()) > 0

def validate_phone(phone):
    return re.fullmatch(r'\+?\d{7,15}', phone) is not None

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None
