with open('index.html', 'r') as f:
    html = f.read()

# Remove 'opacity: 1 !important;' from the inline styles
html = html.replace('opacity: 1 !important; ', '')

with open('index.html', 'w') as f:
    f.write(html)
print("Opacity override removed.")
