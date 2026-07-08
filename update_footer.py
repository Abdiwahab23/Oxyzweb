import glob
import re

html_files = glob.glob('*.html')
count_total = 0

old_img_pattern = re.compile(r'<img\s+src="images/oxyzcell-1\.webp"\s+alt="OXYZ Health"\s+style="height:\s*50px;\s*margin-bottom:\s*20px;?"\s*\/?>')
new_img = '<img src="images/Logo.png" alt="OXYZ Health" style="height: 50px; margin-bottom: 20px;">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content, count = old_img_pattern.subn(new_img, content)
    
    if count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer logo in {file}")
        count_total += count
    else:
        # Maybe it's slightly different, just search and replace the src inside footer
        if 'images/oxyzcell-1.webp' in content:
            content = content.replace('images/oxyzcell-1.webp', 'images/Logo.png')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fallback: Updated images/oxyzcell-1.webp to images/Logo.png in {file}")
            count_total += 1

print(f"Total replacements: {count_total}")
