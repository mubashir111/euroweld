with open('index.html', 'r') as f:
    html = f.read()

# Replace broken download icon with simple text arrow or unicode character
html = html.replace('<i class="icofont-download icon-space-right"></i>', '&#x2193;')
html = html.replace('<i\n                                                class="icofont-paper-plane"></i>', '&#x279C;')
html = html.replace('<i class="icofont-paper-plane"></i>', '&#x279C;')

with open('index.html', 'w') as f:
    f.write(html)
print("Icons fixed.")
