import re

with open('service-list.html', 'r') as f:
    content = f.read()

services_html = """                <div class="service-display-wrapper">
                    <!-- SECTION 1: CORE WELDING CAPABILITIES -->
                    <div class="row mb-6">
                        <div class="col-12">
                            <h3 class="title mb-4">Core Welding Capabilities</h3>
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-1.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">TIG Welding</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Specializing in high-precision, clean finish stainless steel fabrication for commercial kitchens, food processing facilities, and architectural features.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-2.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">MIG/MAG Welding</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Heavy-duty structural carbon steel fabrication for industrial equipment, framing, and machinery. Fast turnaround times for bulk batches.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-3.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">MMA/Arc Welding</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Robust, all-weather field welding for heavy construction, pipeline reinforcement, and structural repairs.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-4.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">Plasma Cutting</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Precision CNC and manual plasma cutting for thick metal plates and custom industrial components.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                        </div>
                    </div>

                    <!-- SECTION 2: TURNKEY INDUSTRIAL SERVICES -->
                    <div class="row">
                        <div class="col-12">
                            <h3 class="title mb-4 mt-4">Turnkey Industrial Services</h3>
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-5.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">Metal Fabrication</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Custom sheet metal and structural component assembly. Complete drawing interpretation, prototyping, and end-to-end component manufacturing.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-6.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">Welding Inspection</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Non-destructive testing (NDT), defect checking, and safety compliance certification to ensure parts align perfectly with global standards.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                            <!-- Start Service Single Item -->
                            <div class="service-single-item">
                                <div class="icon">
                                    <img class="img-fluid" src="assets/images/icons/service-icon-1.png" alt="">
                                </div>
                                <div class="content">
                                    <h4 class="title">On-site Installation</h4>
                                    <p class="mb-4" style="color: #bcbcbc;">Deployable engineering teams for field assembly, structural rigging, and seamless integration of fabricated components.</p>
                                    <a href="service-details.html" class="btn btn-sm btn-outline-primary text-uppercase">
                                        <span>details <i class="icon-space-left">&gt;&gt;</i></span> </a>
                                </div>
                            </div>
                            <!-- End Service Single Item -->
                        </div>
                    </div>
                </div>"""

pattern = r'<div class="service-display-wrapper">.*?</div>\s*</div>\s*</div>'
# Wait, the structure is:
# <div class="service-display-wrapper">
#    <div class="row">
#        <div class="col-12">
#            <!-- items -->
#        </div>
#    </div>
# </div>

pattern = re.compile(r'<div class="service-display-wrapper">.*?</div>\s*</div>\s*</div>', re.DOTALL)
new_content = pattern.sub(services_html, content)

# Fix booking text
new_content = new_content.replace('It is long established fact that a reader will\\n                                distracted by the reasdable.', 'Schedule an on-site consultation or request a technical capabilities review with our engineering support team.')
new_content = new_content.replace('It is long established fact that a reader will\n                                distracted by the reasdable.', 'Schedule an on-site consultation or request a technical capabilities review with our engineering support team.')

# Fix form options
new_content = new_content.replace('<option value="">Fuel Mining</option>', '<option value="">Energy & Utilities</option>')
new_content = new_content.replace('<option value="">Cole Mining</option>', '<option value="">Industrial Manufacturing</option>')
new_content = new_content.replace('<option value="">Gold Mining</option>', '<option value="">Mechanical Engineering</option>')

# Fix recent news in footer
old_news = """                                    <li>
                                        <a href="blog-details.html" class="image">
                                            <img src="assets/images/blog/blog-list-img-1.png" alt="">
                                        </a>
                                        <div class="content">
                                            <a class="title" href="blog-details.html">Recent trends in robotic welding
                                                and type industry.</a>
                                            <span class="date">03 February, 2021</span>
                                        </div>
                                    </li>"""

new_news = """                                    <li>
                                        <a href="#" class="image">
                                            <img src="assets/images/icons/sm-gear-icon.png" alt="" style="background: #ff5e14; padding: 10px; border-radius: 5px;">
                                        </a>
                                        <div class="content">
                                            <a class="title" href="#">ISO 9001:2015 Quality Management Certified</a>
                                            <span class="date">Verified Supplier</span>
                                        </div>
                                    </li>"""

# Replace only the SECOND instance of the duplicate news
parts = new_content.split(old_news)
if len(parts) >= 3:
    new_content = parts[0] + old_news + parts[1] + new_news + parts[2]

with open('service-list.html', 'w') as f:
    f.write(new_content)
