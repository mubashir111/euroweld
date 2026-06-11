with open('index.html', 'r') as f:
    html = f.read()

# Revert blog header
html = html.replace('TECHNICAL RESOURCES', 'LATEST UPDATES')
html = html.replace('WHITEPAPERS & GUIDES', 'WELDING NEWS')

# Revert blog post dates
html = html.replace('PDF Download', '03.02.2021')
html = html.replace('Whitepaper: Safety Protocols in High-Pressure Gas Flow', 'How to choose the right welding accessories for high-pressure environments.')
html = html.replace('Technical Guide: Maximizing Output with Automated Welding', 'Advancements in energy-efficient welding equipment and sustainable manufacturing.')

with open('index.html', 'w') as f:
    f.write(html)
print("Blog copy reverted.")
