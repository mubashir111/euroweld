import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Header & Navigation

# Apply align-items: center to the header navigation (assuming the container is a flexbox like .header-wrapper or similar).
# Actually, I can just add inline CSS to the header row or check if there is a class I can target.
# Looking at the header, usually there's a `.header-nav` or `.header-wrapper`.
# Let's do it in CSS. But we can also add it to the brochure button directly.
# Let's find the brochure button:
html = html.replace('href="assets/Euroweld-Brochure.pdf"', 'href="assets/Euroweld-Brochure.pdf" style="padding-top: 8px; padding-bottom: 8px;"')

# Increase opacity of social icons:
# Let's find the social icons in the header
html = html.replace('class="header-top-social"', 'class="header-top-social" style="opacity: 0.9;"')

# 2. Hero Section
# Add text shadow to headings
html = html.replace('class="title"', 'class="title" style="text-shadow: 2px 2px 5px rgba(0,0,0,0.7);"')

# Add bottom margin to Request Custom Quote button
html = html.replace('class="btn btn-lg btn-default btn-orange"', 'class="btn btn-lg btn-default btn-orange" style="margin-bottom: 30px;"')

# 3. Content
# Pillars
html = html.replace('Premium Quality', 'Expert Support')
html = html.replace('Expert Team', 'Certified Quality')
html = html.replace('Excellent Service', 'Global Distribution')

# Blog dates
html = html.replace('03.02.2021', '14.05.2026', 1)
html = html.replace('03.02.2021', '22.04.2026', 1)

# 4. Technical Fixes
# Back-to-Top Button z-index
html = html.replace('class="scroll-top"', 'class="scroll-top" style="z-index: 9999;"')

with open('index.html', 'w') as f:
    f.write(html)
print("Final polish applied to index.html")
