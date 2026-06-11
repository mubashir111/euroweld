import re

with open('service-list.html', 'r') as f:
    html = f.read()

# Replace the current wrapper and headings
old_html = """                <div class="service-display-wrapper">
                    <!-- SECTION 1: CORE WELDING CAPABILITIES -->
                    <div class="row mb-6">
                        <div class="col-12">
                            <h3 class="title mb-4">Core Welding Capabilities</h3>"""

new_html = """                <!-- SECTION 1: CORE WELDING CAPABILITIES -->
                <div class="section-content">
                    <h3 class="title mb-4">Core Welding Capabilities</h3>
                </div>
                <div class="service-display-wrapper mb-6">
                    <div class="row">
                        <div class="col-12">"""

html = html.replace(old_html, new_html)

old_html2 = """                    <!-- SECTION 2: TURNKEY INDUSTRIAL SERVICES -->
                    <div class="row">
                        <div class="col-12">
                            <h3 class="title mb-4 mt-4">Turnkey Industrial Services</h3>"""

new_html2 = """                </div>
                
                <!-- SECTION 2: TURNKEY INDUSTRIAL SERVICES -->
                <div class="section-content mt-6">
                    <h3 class="title mb-4">Turnkey Industrial Services</h3>
                </div>
                <div class="service-display-wrapper">
                    <div class="row">
                        <div class="col-12">"""

html = html.replace(old_html2, new_html2)

with open('service-list.html', 'w') as f:
    f.write(html)
