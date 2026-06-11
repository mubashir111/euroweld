with open('index.html', 'r') as f:
    html = f.read()

# 1. Revert global mistake
html = html.replace('class="title" style="text-shadow: 2px 2px 5px rgba(0,0,0,0.7);"', 'class="title"')

# 2. Add text shadow ONLY to hero titles
# Hero titles usually look like <h2 class="title">...</h2> inside .hero-content
# We can search for the specific lines. Let's just use string replacement on the exact hero titles if we know them.
# The titles are: "PROFESSIONAL WELDING <br> EQUIPMENT & ACCESSORIES", "PRECISION BRASS <br> GAS REGULATORS", etc.
# Or better, we can find `<div class="hero-content">` and replace `<h2 class="title">` inside it.
import re
def hero_shadow_replacer(match):
    return match.group(1) + '<h2 class="title" style="text-shadow: 2px 2px 5px rgba(0,0,0,0.7); color: #fff;">'

html = re.sub(r'(<div class="hero-content">[\s\S]*?)<h2 class="title">', hero_shadow_replacer, html)

with open('index.html', 'w') as f:
    f.write(html)
print("Readability fixed.")
