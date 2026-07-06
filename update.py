import glob

social_old = '''          <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
          </div>'''

social_new = '''          <div class="social-links">
            <a href="https://www.facebook.com/OXYZHealthInternational"><i class="fab fa-facebook-f"></i></a>
            <a href="https://instagram.com/oxyzinter"><i class="fab fa-instagram"></i></a>
            <a href="https://international.oxyzhealth.com"><i class="fas fa-globe"></i></a>
          </div>'''

contact_old = '''            <li >
              <i
                class="fas fa-map-marker-alt"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              Malaysia & Singapore
            </li>
            <li >
              <i
                class="fas fa-envelope"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              contact@oxyzhealth.com
            </li>
            <li >
              <i
                class="fas fa-phone"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              +60 123 456 789
            </li>'''

contact_new = '''            <li >
              <i
                class="fas fa-map-marker-alt"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              Irving Pl, #1-26, Singapore 369546
            </li>
            <li >
              <i
                class="fas fa-envelope"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              contact@oxyzhealth.com
            </li>
            <li >
              <i
                class="fas fa-phone"
                style="margin-right: 10px; color: var(--gold)"
              ></i>
              +65 8616 3762
            </li>'''

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    if social_old in content:
        content = content.replace(social_old, social_new)
        print(f + ' updated social')
        modified = True
    if contact_old in content:
        content = content.replace(contact_old, contact_new)
        print(f + ' updated contact')
        modified = True
        
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
