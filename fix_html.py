import os
import re
import glob

desktop_nav_replacement = """<ul class="header-nav" style="align-items: center;">
                                <li><a href="index.html">Home</a></li>
                                <li><a href="about.html">About Us</a></li>
                                <li><a href="service-list.html">Services</a></li>
                                <li><a href="products.html">Product</a></li>
                                <li><a href="contact.html">Contact</a></li>
                            </ul>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace broken desktop nav
    content = re.sub(r'<ul\s+class="header-nav"[^>]*>.*?<!-- End Header Logo -->', desktop_nav_replacement + '\n                            <!-- End Header Logo -->', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("HTML repaired across all files.")
