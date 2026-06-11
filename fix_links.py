import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, "r") as f:
        content = f.read()

    # Replace href="#" with href="javascript:void(0);"
    new_content = content.replace('href="#"', 'href="javascript:void(0);"')

    # Replace mailto:info@euroweld.co.uk with contact.html
    new_content = new_content.replace('href="mailto:info@euroweld.co.uk"', 'href="contact.html"')
    
    # Also fix action="#" just in case since they aren't using formspree yet
    new_content = new_content.replace('action="#"', 'action="javascript:void(0);"')

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)

print("Links and actions fixed.")
