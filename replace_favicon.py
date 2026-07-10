import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('href="images/favicon_white.png"', 'href="images/Logo%202.png"')
    content = content.replace('href="images/favicon.jpg"', 'href="images/Logo%202.png"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print('Updated favicon in', f)
