import os
import re

directory = 'd:/Oxyzcell'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

new_block = """        <div class="footer-col">
          <h4>Contact Us</h4>
          <ul class="footer-links">
            <li style="display: flex; align-items: center; margin-bottom: 15px;">
              <i class="far fa-envelope" style="margin-right: 12px; color: var(--gold); font-size: 1.1rem;"></i>
              global@oxyzhealth.com
            </li>
            <li style="display: flex; align-items: center; margin-bottom: 15px;">
              <i class="fas fa-phone-alt" style="margin-right: 12px; color: var(--gold); font-size: 1.1rem;"></i>
              +65 8616 3762
            </li>
            <li style="display: flex; align-items: center; margin-bottom: 15px;">
              <i class="fas fa-map-marker-alt" style="margin-right: 12px; color: var(--gold); font-size: 1.1rem;"></i>
              USA | Singapore | Malaysia
            </li>
          </ul>
        </div>"""

# Match the entire footer-col containing Contact Us
pattern = re.compile(r'<div class="footer-col">\s*<h4>Contact Us</h4>\s*<ul class="footer-links">.*?</ul>\s*</div>', re.DOTALL)

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub(new_block, content)

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
