import os
import glob

html_files = glob.glob('d:/Oxyzcell/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content.replace('images/oxyzcell-1.webp', 'images/Logo.png')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
