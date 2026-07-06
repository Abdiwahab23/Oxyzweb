import glob

nav_old = '''      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="oxyz-cell.html">Stem Cell</a>
        <a href="bioseries.html">BioSeries</a>
        <a href="training.html">Training &amp; Consultation</a>
        <a href="contact.html">Contact Us</a>
      </div>'''

nav_new = '''      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="bioseries.html">BioSeries</a>
        <a href="oxyz-cell.html">Stem Cell</a>
        <a href="training.html">Training &amp; Consultation</a>
        <a href="about.html">About Us</a>
        <a href="contact.html">Contact Us</a>
      </div>'''

nav_old_2 = '''      <div class="nav-links">
        <a href="index.html" class="active">Home</a>
        <a href="about.html">About Us</a>
        <a href="oxyz-cell.html">Stem Cell</a>
        <a href="bioseries.html">BioSeries</a>
        <a href="training.html">Training &amp; Consultation</a>
        <a href="contact.html">Contact Us</a>
      </div>'''

nav_new_2 = '''      <div class="nav-links">
        <a href="index.html" class="active">Home</a>
        <a href="bioseries.html">BioSeries</a>
        <a href="oxyz-cell.html">Stem Cell</a>
        <a href="training.html">Training &amp; Consultation</a>
        <a href="about.html">About Us</a>
        <a href="contact.html">Contact Us</a>
      </div>'''

# Sometimes they have an active class, let's just do a more robust regex or replace
import re

def reorder_nav(content):
    # Find the nav-links div
    pattern = r'(<div class="nav-links">\s*)(.*?)(\s*</div>)'
    
    def replacer(match):
        prefix = match.group(1)
        links_str = match.group(2)
        suffix = match.group(3)
        
        # Extract individual links
        links = re.findall(r'<a.*?</a>', links_str)
        
        # We know the specific links we have
        home = next((l for l in links if 'Home' in l), None)
        bio = next((l for l in links if 'BioSeries' in l), None)
        stem = next((l for l in links if 'Stem Cell' in l), None)
        training = next((l for l in links if 'Training' in l), None)
        about = next((l for l in links if 'About Us' in l), None)
        contact = next((l for l in links if 'Contact Us' in l), None)
        
        ordered_links = [l for l in [home, bio, stem, training, about, contact] if l]
        # Any other links that might exist
        for l in links:
            if l not in ordered_links:
                ordered_links.append(l)
                
        return prefix + '\n        '.join(ordered_links) + suffix
        
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def reorder_footer(content):
    # Find the footer-links ul under Quick Links
    pattern = r'(<h4>Quick Links</h4>\s*<ul class="footer-links">\s*)(.*?)(\s*</ul>)'
    
    def replacer(match):
        prefix = match.group(1)
        links_str = match.group(2)
        suffix = match.group(3)
        
        # Extract individual li elements
        links = re.findall(r'<li.*?</li>', links_str, re.DOTALL)
        
        # Order them similarly
        home = next((l for l in links if 'Home' in l), None)
        bio = next((l for l in links if 'BioSeries' in l), None)
        stem = next((l for l in links if 'Stem Cell' in l), None)
        training = next((l for l in links if 'Training' in l), None)
        about = next((l for l in links if 'About Us' in l), None)
        contact = next((l for l in links if 'Contact Us' in l), None)
        
        ordered_links = [l for l in [home, bio, stem, training, about, contact] if l]
        
        return prefix + '\n            '.join(ordered_links) + suffix
        
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = reorder_nav(content)
    new_content = reorder_footer(new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f + ' updated nav/footer links')
