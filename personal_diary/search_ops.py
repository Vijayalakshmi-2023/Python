# search_ops.py

def search_by_date(entries, target_date):
    return [e for e in entries if e['date'] == target_date]

def search_by_tag(entries, tag):
    return [e for e in entries if tag in e['tags']]

def summary(entries):
    total = len(entries)
    all_tags = set()
    for e in entries:
        all_tags.update(e['tags'])
    return total, all_tags
