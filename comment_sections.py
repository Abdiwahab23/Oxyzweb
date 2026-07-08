import re

with open('d:/Oxyzcell/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

section1_start = content.find("<!-- Section: The Catalogue -->")
section1_end_str = "Exclusively Made in USA\n          </div>\n        </div>\n      </div>\n    </section>"
section1_end = content.find(section1_end_str)

if section1_end != -1:
    section1_end += len(section1_end_str)

if section1_start != -1 and section1_end != -1:
    sub = content[section1_start:section1_end]
    sub = sub.replace("<!--", "<!-").replace("-->", "->")
    content = content[:section1_start] + "<!-- HIDING SECTIONS\n    " + sub + "\n    HIDING SECTIONS END -->" + content[section1_end:]

tier_start_str = '        <div class="grid-2" style="gap: 20px;">\n          <!-- Tier 01 -->'
tier_start = content.find(tier_start_str)

tier_end_str = 'Capital partnership into regional manufacturing, clinic rollout or market entry.</p>\n          </div>\n        </div>'
tier_end = content.find(tier_end_str)

if tier_end != -1:
    tier_end += len(tier_end_str)

if tier_start != -1 and tier_end != -1:
    sub = content[tier_start:tier_end]
    sub = sub.replace("<!--", "<!-").replace("-->", "->")
    content = content[:tier_start] + "<!-- HIDING TIERS\n" + sub + "\n        HIDING TIERS END -->" + content[tier_end:]

with open('d:/Oxyzcell/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"section1: {section1_start} to {section1_end}")
print(f"tiers: {tier_start} to {tier_end}")
