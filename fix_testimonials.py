import re

with open('index.html', 'r') as f:
    html = f.read()

# Make all 7 testimonial images circular
for i in range(1, 8):
    old_img = f'<img src="assets/images/testimonial/testimonial-person-{i}.png" alt="">'
    new_img = f'<img src="assets/images/testimonial/testimonial-person-{i}.png" style="border-radius: 50%; object-fit: cover; width: 75px; height: 75px;" alt="">'
    html = html.replace(old_img, new_img)
    
    old_img2 = f'<img src="assets/images/testimonial/testimonial-person-{i}.png" alt="image">'
    new_img2 = f'<img src="assets/images/testimonial/testimonial-person-{i}.png" style="border-radius: 50%; object-fit: cover; width: 75px; height: 75px;" alt="image">'
    html = html.replace(old_img2, new_img2)

# Add 5-star rating beneath the designation
star_html = '\n                                    <div style="color: #E99640; font-size: 18px; margin-top: 10px;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
html = re.sub(r'(<span class="designation">.*?</span>)', r'\1' + star_html, html)

with open('index.html', 'w') as f:
    f.write(html)
print("Testimonial styles and stars updated.")
