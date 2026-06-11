import re

# Update service-list.html
with open('service-list.html', 'r') as f:
    html = f.read()

html = html.replace('GET UPDATE EVERYTHING', 'GET THE LATEST WELDING INSIGHTS')
html = html.replace('euroweld_logo.png', 'logo.png')
html = html.replace('Recent trends in robotic welding\n                                                and type industry.', 'Recent trends in robotic welding AND THE MANUFACTURING SECTOR.')
html = html.replace('Recent trends in robotic welding and type industry.', 'Recent trends in robotic welding AND THE MANUFACTURING SECTOR.')
html = html.replace('03 February, 2021', 'Verified Insight')
html = html.replace('<i class="icofont-paper-plane"></i>', '&#x27A4;')

with open('service-list.html', 'w') as f:
    f.write(html)

# Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Fix the footer nav icon
css = css.replace('content: "\\ea94";\n  font-family: "IcoFont";', 'content: "\\00BB";\n  font-family: sans-serif;')
css = css.replace('content: "\\ea94";', 'content: "\\00BB";')

# Append new styles
new_css = """
/* Brighten the footer typography for perfect readability */
footer, .contact-us, .recent-news {
    color: #E0E0E0 !important;
}

footer a, .recent-news a {
    color: #FFFFFF !important;
    text-decoration: none;
}

footer a:hover {
    color: #E99640 !important;
}

/* Ensure email input text is highly visible */
.newsletter-form-group input {
    color: #FFFFFF !important;
}
"""

with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

