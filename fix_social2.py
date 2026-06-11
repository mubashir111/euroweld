with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the previous fix with !important to ensure it overrides everything
old_rule = '''
.header-bottom:not(.is-sticky) .social-link-white a {
  border: 2px solid rgba(255, 255, 255, 0.7);
  color: #fff;
  opacity: 1;
}
'''

new_rule = '''
.header-bottom:not(.is-sticky) .social-link-white a {
  border: 2px solid rgba(255, 255, 255, 0.7) !important;
  color: #fff !important;
  opacity: 1 !important;
}

.is-sticky .social-link-white a {
  border: 2px solid #111 !important;
  color: #111 !important;
  opacity: 0.9 !important;
}
'''

css = css.replace(old_rule, new_rule)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Social link CSS updated with !important.")
