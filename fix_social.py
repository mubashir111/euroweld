import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove the hardcoded white inline styles from social links
html = html.replace('style="color: #ffffff !important; border-color: rgba(255,255,255,0.7) !important;" ', '')
html = html.replace('style="margin-right: 15px; opacity: 1 !important;"', 'style="margin-right: 15px;"')

with open('index.html', 'w') as f:
    f.write(html)

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the #111 rule so it only applies when the header is sticky or on mobile
# Actually, the sticky class is added to .sticky-header, which is .header-bottom
# Let's change `.header-bottom .social-link-white a` to `.is-sticky .social-link-white a`
# And make the default `.header-bottom .social-link-white a` white.

css = css.replace('.header-bottom .social-link-white a,', '.is-sticky .social-link-white a,')

# Add a specific rule for non-sticky header-bottom so they are white
css += '''
.header-bottom:not(.is-sticky) .social-link-white a {
  border: 2px solid rgba(255, 255, 255, 0.7);
  color: #fff;
  opacity: 1;
}
'''

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Social link CSS fixed.")
