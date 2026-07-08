import glob
import os

html_files = glob.glob('d:/Oxyzcell/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the old js link with a cache-busting version
    new_content = content.replace('"js/script.js?v=4"', '"js/script.js?v=5"')
    new_content = new_content.replace('"js/script.js?v=3"', '"js/script.js?v=5"')
    new_content = new_content.replace('"js/script.js"', '"js/script.js?v=5"')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Busted JS cache in {file_path}")
