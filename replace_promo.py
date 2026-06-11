import re

with open('index.html', 'r') as f:
    content = f.read()

new_promo = """<!-- .....:::::: Start Promo Section :::::.... -->
        <div class="promo-section">
            <div class="promo-wrapper">
                <!-- Start Single Promo Singel Item -->
                <div class="promo-single-item">
                    <div class="box">
                        <div class="icon">
                            <img src="assets/images/icons/promo-icon-1.png" alt="Ready Stock">
                        </div>
                        <div class="content">
                            <h4 class="title">Ready Stock</h4>
                            <p>Massive inventory of welding equipment available for immediate dispatch.</p>
                        </div>
                    </div>
                </div>
                <!-- End Single Promo Singel Item -->
                <!-- Start Single Promo Singel Item -->
                <div class="promo-single-item">
                    <div class="box">
                        <div class="icon">
                            <img src="assets/images/icons/promo-icon-3.png" alt="Fast Delivery">
                        </div>
                        <div class="content">
                            <h4 class="title">Fast Delivery</h4>
                            <p>Global logistics network ensuring your projects stay strictly on schedule.</p>
                        </div>
                    </div>
                </div>
                <!-- End Single Promo Singel Item -->
                <!-- Start Single Promo Singel Item -->
                <div class="promo-single-item">
                    <div class="box">
                        <div class="icon">
                            <img src="assets/images/icons/promo-icon-2.png" alt="Quality Assured">
                        </div>
                        <div class="content">
                            <h4 class="title">Quality Assured</h4>
                            <p>Certified equipment passing rigorous international safety and performance standards.</p>
                        </div>
                    </div>
                </div>
                <!-- End Single Promo Singel Item -->
                <!-- Start Single Promo Singel Item -->
                <div class="promo-single-item">
                    <div class="box">
                        <div class="icon">
                            <img src="assets/images/icons/promo-icon-1.png" alt="Technical Support">
                        </div>
                        <div class="content">
                            <h4 class="title">Technical Support</h4>
                            <p>Dedicated engineers providing expert troubleshooting and project consultation.</p>
                        </div>
                    </div>
                </div>
                <!-- End Single Promo Singel Item -->
            </div>
        </div>
        <!-- .....:::::: End Promo Section :::::.... -->"""

content = re.sub(r'<!-- \.\.\.\.\.\:\:\:\:\:\: Start Promo Section \:\:\:\:\:\.\.\.\. -->.*?<!-- \.\.\.\.\.\:\:\:\:\:\: End Promo Section \:\:\:\:\:\.\.\.\. -->', new_promo, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Promo section updated.")
