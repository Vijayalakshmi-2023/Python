# scanner.py

import os

def scan_directory(path):
    file_dict = {}
    file_types = set()

    for root, _, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1].lower().lstrip('.')
            if ext:
                file_types.add(ext)
                file_dict.setdefault(ext, []).append(os.path.join(root, file))

    return file_dict, file_types
