import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove RECENT NEWS column
    content = re.sub(r'<div class="col-[^>]+>\s*<div class="footer-widget-single-item">\s*<h3 class="title">RECENT NEWS</h3>.*?</div>\s*</div>\s*</div>', '</div>', content, flags=re.DOTALL)
    
    # Remove QUICK LINKS column
    content = re.sub(r'<div class="col-[^>]+>\s*<div class="footer-widget-single-item">\s*<h3 class="title">QUICK LINKS</h3>.*?</div>\s*</div>\s*</div>', '</div>', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Unwanted footer columns removed.")
