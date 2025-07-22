# search/search_ops.py

def search_by_name(records, name):
    return [rec for rec in records if name.lower() in rec["id"][1].lower()]

def search_by_department(records, dept):
    return [rec for rec in records if dept.lower() in rec["department"].lower()]
