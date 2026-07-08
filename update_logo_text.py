import os
import glob
import re

html_files = glob.glob('d:/Oxyzcell/*.html')

logo_pattern = re.compile(r'<a href="index\.html" class="logo"[\s\S]*?<img src="images/Logo\.png"[^>]*>[\s\S]*?</a>')

replacement = '''<a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none;">
        <img src="images/Logo.png" alt="OXYZ Health & Wellness" style="height: 40px" />
        <span class="logo-text">OXYZ <span class="logo-text-gold">Health & Wellness</span></span>
      </a>'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = logo_pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
