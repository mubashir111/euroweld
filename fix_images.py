import glob
import re
import os

def process_img_tag(match):
    img_tag = match.group(0)
    
    # 1. Add loading="lazy" if appropriate
    if "loading=" not in img_tag:
        lazy_folders = ["/blog/", "/service/", "/project/", "/product/", "/about/"]
        src_match = re.search(r'src="([^"]+)"', img_tag)
        if src_match:
            src = src_match.group(1)
            if any(folder in src for folder in lazy_folders):
                img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
                
    # 2. Fix empty or missing alt tags
    alt_match = re.search(r'alt="([^"]*)"', img_tag)
    src_match = re.search(r'src="([^"]+)"', img_tag)
    
    if src_match:
        src = src_match.group(1)
        filename = os.path.basename(src).split('.')[0]
        descriptive_alt = filename.replace('-', ' ').replace('_', ' ').title()
        
        if not alt_match:
            # Add alt tag
            img_tag = img_tag.replace('<img ', f'<img alt="{descriptive_alt}" ')
        elif alt_match.group(1).strip() == "":
            # Replace empty alt tag
            img_tag = img_tag.replace('alt=""', f'alt="{descriptive_alt}"')

    return img_tag

for filepath in glob.glob("*.html"):
    with open(filepath, "r") as f:
        content = f.read()

    new_content = re.sub(r'<img [^>]+>', process_img_tag, content)

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)

print("Images optimized.")
