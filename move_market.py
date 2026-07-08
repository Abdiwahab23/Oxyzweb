import sys

with open('d:/Oxyzcell/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

market_start = content.find('        <!-- Section: Market Opportunity -->\n    <section class="section">')
if market_start == -1:
    print("Could not find market opportunity start")
    sys.exit(1)

market_end_str = '        </div>\n      </div>\n    </section>\n'
market_end = content.find(market_end_str, market_start)
if market_end == -1:
    print("Could not find market opportunity end")
    sys.exit(1)
market_end += len(market_end_str)

market_block = content[market_start:market_end]

# Remove the block from its current location
content = content[:market_start] + content[market_end:]

# Insert it before Global Partnerships
partner_start = content.find('<!-- Section 6: Global Partnerships -->')
if partner_start == -1:
    print("Could not find global partnerships start")
    sys.exit(1)

content = content[:partner_start] + market_block + content[partner_start:]

with open('d:/Oxyzcell/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Moved successfully.")
