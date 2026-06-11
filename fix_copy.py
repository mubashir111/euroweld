with open('index.html', 'r') as f:
    html = f.read()

# Update blog header
html = html.replace('LATEST UPDATES', 'TECHNICAL RESOURCES')
html = html.replace('WELDING NEWS', 'WHITEPAPERS & GUIDES')

# Update blog post dates
html = html.replace('03.02.2021', 'PDF Download')
html = html.replace('How to choose the right welding accessories for high-pressure environments.', 'Whitepaper: Safety Protocols in High-Pressure Gas Flow')
html = html.replace('Advancements in energy-efficient welding equipment and sustainable manufacturing.', 'Technical Guide: Maximizing Output with Automated Welding')

# Update about company copy
html = html.replace('providing the best welding solutions for professional users', 'delivering high-performance, precision-engineered solutions')
html = html.replace('meet the highest international benchmarks', 'engineered in compliance with AWS (American Welding Society) and EN ISO specifications')

with open('index.html', 'w') as f:
    f.write(html)
print("Copy updated.")
