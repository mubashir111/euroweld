with open('index.html', 'r') as f:
    lines = f.readlines()

# project-display-section ends at line 744 (index 743)
# The block to move (Testimonial, Logo, Blog) is from line 745 to 1057 (indices 744 to 1056)
# The block to move up (RFQ form) is from line 1058 to 1130 (indices 1057 to 1129)

# We want to insert the RFQ form block BEFORE the Testimonial block.
# Since the RFQ form is directly after the Testimonial/Blog block, we just swap them!

rfq_block = lines[1057:1130]
testimonial_blog_block = lines[744:1057]

# The new middle section is rfq_block + testimonial_blog_block
new_lines = lines[:744] + rfq_block + testimonial_blog_block + lines[1130:]

with open('index.html', 'w') as f:
    f.writelines(new_lines)

print("HTML reordered successfully.")
