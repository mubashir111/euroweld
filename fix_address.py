import re
import glob

footer_about_replacement = """<ul class="footer-about">
                                    <li>
                                        <div class="text"><span class="text-marker">Company:</span>EUROWELD SCHWEISSTECHNIK UK LTD.</div>
                                    </li>
                                    <li>
                                        <div class="text"><span class="text-marker">Location:</span>5 BRAYFORD SQUARE, LONDON, E1 0SG, UNITED KINGDOM</div>
                                    </li>
                                    <li>
                                        <div class="text"><span class="text-marker">Phone:</span><a href="tel:+441234567890">+44 123 456 7890</a></div>
                                    </li>
                                    <li>
                                        <div class="text"><span class="text-marker">Web:</span><a href="http://www.euroweld.co.uk">www.euroweld.co.uk</a></div>
                                    </li>
                                    <li>
                                        <div class="text"><span class="text-marker">Email:</span> <a href="mailto:info@euroweld.co.uk">info@euroweld.co.uk</a> </div>
                                    </li>
                                </ul>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace footer-about block
    content = re.sub(r'<ul\s+class="footer-about"[^>]*>.*?</ul>', footer_about_replacement, content, flags=re.DOTALL)
    
    if filepath == 'contact.html':
        # Replace address
        content = re.sub(r'<h3\s+class="info-text">\s*Unit\s+[^<]+</h3>', '<h3 class="info-text">5 BRAYFORD SQUARE, LONDON, E1 0SG, UNITED KINGDOM</h3>', content)
        # Replace email
        content = re.sub(r'<h3\s+class="info-text">\s*<a\s+href="mailto:[^"]+">[^<]+</a>\s*</h3>', '<h3 class="info-text"><a href="mailto:info@euroweld.co.uk">info@euroweld.co.uk</a></h3>', content)
        # Replace web
        content = re.sub(r'<h3\s+class="info-text">\s*<a\s+href="(?:http://|https://)?[^"]+">www\.[^<]+</a>\s*</h3>', '<h3 class="info-text"><a href="http://www.euroweld.co.uk">www.euroweld.co.uk</a></h3>', content)
        content = re.sub(r'<h3\s+class="info-text">\s*<a\s+href="index\.html">www\.[^<]+</a>\s*</h3>', '<h3 class="info-text"><a href="http://www.euroweld.co.uk">www.euroweld.co.uk</a></h3>', content)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Contact information updated across all HTML files.")
