import os
import re
import glob

desktop_nav_replacement = """<ul class="header-nav">
                                <li><a href="index.html">Home</a></li>
                                <li><a href="about.html">About Us</a></li>
                                <li><a href="service-list.html">Services</a></li>
                                <li><a href="products.html">Product</a></li>
                                <li><a href="contact.html">Contact</a></li>
                            </ul>"""

mobile_nav_replacement = """<div class="offcanvas-menu">
                        <ul>
                            <li><a href="index.html"><span>Home</span></a></li>
                            <li><a href="about.html"><span>About Us</span></a></li>
                            <li><a href="service-list.html"><span>Services</span></a></li>
                            <li><a href="products.html"><span>Product</span></a></li>
                            <li><a href="contact.html"><span>Contact</span></a></li>
                        </ul>
                    </div>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace desktop nav
    # Matches <ul class="header-nav"...>...</ul>
    content = re.sub(r'<ul\s+class="header-nav"[^>]*>.*?</ul>', desktop_nav_replacement, content, flags=re.DOTALL)
    
    # Replace mobile nav
    # Matches <div class="offcanvas-menu">...</div>
    content = re.sub(r'<div\s+class="offcanvas-menu">.*?</div>\s*<!-- End Mobile Menu Nav -->', mobile_nav_replacement + ' <!-- End Mobile Menu Nav -->', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Navigation updated across all HTML files.")
