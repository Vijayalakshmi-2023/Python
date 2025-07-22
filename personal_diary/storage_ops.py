# storage_ops.py

import json
from os.path import exists

FILE = "diary.json"

def load_entries():
    if not exists(FILE):
        return []
    with open(FILE, 'r') as f:
        raw = json.load(f)
        # Convert tag lists back to sets
        for entry in raw:
            entry['tags'] = set(entry['tags'])
        return raw

def save_entries(entries):
    # Convert tag sets to lists for JSON
    json_ready = []
    for entry in entries:
        entry_copy = entry.copy()
        entry_copy['tags'] = list(entry_copy['tags'])
        json_ready.append(entry_copy)
    with open(FILE, 'w') as f:
        json.dump(json_ready, f, indent=2)
