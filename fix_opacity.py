with open('index.html', 'r') as f:
    html = f.read()

# Fix hero opacity and color
html = html.replace('class="title-tag" style="', 'class="title-tag" style="color: #ffffff !important; opacity: 1 !important; ')
html = html.replace('class="title" style="', 'class="title" style="color: #ffffff !important; opacity: 1 !important; ')
html = html.replace('class="sub-title" style="', 'class="sub-title" style="color: #ffffff !important; opacity: 1 !important; ')

# Fix social icons color
html = html.replace('<a target="_blank" href="https://www.facebook', '<a target="_blank" style="color: #ffffff !important; border-color: rgba(255,255,255,0.7) !important;" href="https://www.facebook')
html = html.replace('<a target="_blank" href="https://www.twitter', '<a target="_blank" style="color: #ffffff !important; border-color: rgba(255,255,255,0.7) !important;" href="https://www.twitter')
html = html.replace('<a target="_blank" href="https://www.linkedin', '<a target="_blank" style="color: #ffffff !important; border-color: rgba(255,255,255,0.7) !important;" href="https://www.linkedin')

with open('index.html', 'w') as f:
    f.write(html)
print("Opacity and colors fixed.")
