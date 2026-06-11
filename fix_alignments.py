import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix social media icon margin
html = html.replace('<ul class="social-link social-link-white">', '<ul class="social-link social-link-white" style="margin-right: 15px;">')

# Ensure all 3 hero instances have margin-bottom for the h4 and h3, and for the btn
# Hero 1
html = html.replace('<h4 class="title-tag">Welcome to Euroweld</h4>', '<h4 class="title-tag" style="margin-bottom: 25px;">Welcome to Euroweld</h4>')
html = html.replace('<h3 class="sub-title">EQUIPMENT & ACCESSORIES</h3>', '<h3 class="sub-title" style="margin-bottom: 40px;">EQUIPMENT & ACCESSORIES</h3>')

# Hero 2
html = html.replace('<h3 class="sub-title">CONSUMABLES & SPARES</h3>', '<h3 class="sub-title" style="margin-bottom: 40px;">CONSUMABLES & SPARES</h3>')
# Hero 3
html = html.replace('<h3 class="sub-title">SOLUTIONS FOR YOUR PROJECTS</h3>', '<h3 class="sub-title" style="margin-bottom: 40px;">SOLUTIONS FOR YOUR PROJECTS</h3>')

# Ensure buttons have margin-bottom
html = html.replace('style="background: #E99640 !important; border-color: #E99640 !important; text-shadow: none;">', 'style="background: #E99640 !important; border-color: #E99640 !important; text-shadow: none; margin-bottom: 40px;">')

with open('index.html', 'w') as f:
    f.write(html)
print("Alignments fixed.")
