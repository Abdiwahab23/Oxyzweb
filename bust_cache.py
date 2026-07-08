import glob
import os
import re

# 1. Rename files in Training/
image_files = glob.glob('Training/*.jpg')
rename_map = {}

for filepath in image_files:
    if '-opt' not in filepath:
        basename = os.path.basename(filepath)
        name, ext = os.path.splitext(basename)
        new_basename = f"{name}-opt{ext}"
        new_filepath = os.path.join('Training', new_basename)
        
        # Rename the file on disk
        os.rename(filepath, new_filepath)
        rename_map[basename] = new_basename

print(f"Renamed {len(rename_map)} files.")

# 2. Update training.html
with open('training.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for old_name, new_name in rename_map.items():
    if old_name in content:
        content = content.replace(old_name, new_name)
        count += 1

with open('training.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {count} references in training.html.")
