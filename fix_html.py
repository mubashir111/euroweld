import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, "r") as f:
        content = f.read()

    original_content = content

    # 1. Hide Stats section (only in index.html, about.html, etc. wherever it exists)
    content = re.sub(r'(<div class="counter-display-section[^"]*)(">)', r'\1 d-none\2', content)

    # 2. Remove footer phone number
    content = re.sub(r'<li>\s*<div class="text"><span class="text-marker">Phone:</span><a href="tel:\+441234567890">\+44 123 456 7890</a></div>\s*</li>', '', content)

    # 3. Remove footer WhatsApp link
    content = re.sub(r'<li class="mt-3">\s*<a href="https://wa\.me/441234567890"[\s\S]*?Chat on WhatsApp\s*</a>\s*</li>', '', content)

    # 4. Remove contact page phone block
    content = re.sub(r'<div class="contact-info-single-item">\s*<div class="icon">\s*<i class="icofont-phone"></i>\s*</div>\s*<div class="content">\s*<h4 class="title">Phone Number</h4>\s*<h3 class="info-text"><a href="tel:\+441234567890">\+44 123 456 7890</a></h3>\s*</div>\s*</div>', '', content)
    # Since I'm not sure if the wrapper is there, let's also do:
    content = re.sub(r'<h3 class="info-text"><a href="tel:\+441234567890">\+44 123 456 7890</a></h3>', '', content)

    # 5. Fix Catalog Download form
    # It looks like: <form class="form-group" action="javascript:void(0);" method="post">
    # We change it to mailto:
    content = re.sub(
        r'<form class="form-group" action="javascript:void\(0\);" method="post">',
        r'<form class="form-group" action="mailto:info@euroweld.co.uk" method="post" enctype="text/plain">',
        content
    )

    if content != original_content:
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath}")
