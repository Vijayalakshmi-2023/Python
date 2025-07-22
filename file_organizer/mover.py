# mover.py

import os
import shutil

def move_files_by_type(file_dict, target_base):
    for ext, files in file_dict.items():
        folder = os.path.join(target_base, ext)
        os.makedirs(folder, exist_ok=True)

        for file in files:
            try:
                filename = os.path.basename(file)
                dest = os.path.join(folder, filename)
                shutil.move(file, dest)
                print(f"Moved: {filename} → {folder}")
            except Exception as e:
                print(f"❌ Error moving {file}: {e}")
