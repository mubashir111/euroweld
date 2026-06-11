import re

with open('index.html', 'r') as f:
    content = f.read()

# Extract sections
hero_match = re.search(r'(<!-- \.\.\.\.\.\:\:\:\:\:\: Start Hero Section \:\:\:\:\:\.\.\.\. -->.*?<!-- \.\.\.\.\.\:\:\:\:\:\: End Hero Section \:\:\:\:\:\.\.\.\. -->)', content, re.DOTALL)
promo_match = re.search(r'(<!-- \.\.\.\.\.\:\:\:\:\:\: Start Promo Section \:\:\:\:\:\.\.\.\. -->.*?<!-- \.\.\.\.\.\:\:\:\:\:\: End Promo Section \:\:\:\:\:\.\.\.\. -->)', content, re.DOTALL)
about_match = re.search(r'(<!-- \.\.\.\.\.\:\:\:\:\:\: Start About-Display Section \:\:\:\:\:\.\.\.\. -->.*?<!-- \.\.\.\.\.\:\:\:\:\:\: End About-Display Section \:\:\:\:\:\.\.\.\. -->)', content, re.DOTALL)

if not (hero_match and promo_match and about_match):
    print("Could not find all sections.")
    exit(1)

hero = hero_match.group(1)
promo = promo_match.group(1)
about = about_match.group(1)

# Remove promo and about
content = content.replace(promo, '')
content = content.replace(about, '')

# Re-insert About then Promo right after Hero
new_sequence = hero + "\n\n        " + about + "\n\n        " + promo
content = content.replace(hero, new_sequence)

with open('index.html', 'w') as f:
    f.write(content)

print("Reordering complete.")
