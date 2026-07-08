import glob
import os

html_files = glob.glob('d:/Oxyzcell/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the old css link with a cache-busting version
    # If it's already versioned, we could do regex, but let's just replace the exact string
    new_content = content.replace('"css/style.css?v=5"', '"css/style.css?v=6"')
    new_content = new_content.replace('"css/style.css?v=4"', '"css/style.css?v=6"')
    new_content = new_content.replace('"css/style.css"', '"css/style.css?v=6"')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Busted cache in {file_path}")
