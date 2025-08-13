#!/usr/bin/env python3
"""
Verify Social Media Preview Setup
Tests that all meta tags and images are properly configured
"""

import os
import re
from urllib.parse import urljoin


class SocialPreviewVerifier:
    """Verify social media preview configuration"""
    
    def __init__(self, domain='https://skerritteconomics.com'):
        self.domain = domain
        self.errors = []
        self.warnings = []
        self.success = []
    
    def verify_local_setup(self):
        """Verify local file setup"""
        
        print("🔍 Checking local files...")
        print("=" * 50)
        
        # Check for required image files
        required_images = [
            'static/images/seo-preview-1200x630.jpg',
            'static/images/SEC_LOGO.png',
            'static/images/seo-preview-square-1200x1200.jpg',
            'static/images/favicon.ico',
        ]
        
        for image_path in required_images:
            if os.path.exists(image_path):
                size = os.path.getsize(image_path)
                if size > 0:
                    self.success.append(f"✅ Found {image_path} ({size:,} bytes)")
                    
                    # Check image dimensions for main preview
                    if 'seo-preview-1200x630' in image_path:
                        try:
                            from PIL import Image
                            img = Image.open(image_path)
                            width, height = img.size
                            if width == 1200 and height == 630:
                                self.success.append(f"✅ Image dimensions correct: {width}x{height}")
                            else:
                                self.warnings.append(f"⚠️ Image dimensions: {width}x{height} (should be 1200x630)")
                        except:
                            self.warnings.append(f"⚠️ Could not verify image dimensions for {image_path}")
                else:
                    self.errors.append(f"❌ File {image_path} is empty")
            else:
                self.errors.append(f"❌ Missing required file: {image_path}")
        
        # Check template files
        template_files = [
            'templates/partials/_social_previews.html',
            'templates/partials/_meta_tags.html',
            'static/manifest.json'
        ]
        
        for template in template_files:
            if os.path.exists(template):
                self.success.append(f"✅ Found template: {template}")
            else:
                self.errors.append(f"❌ Missing template: {template}")
    
    def verify_meta_tags(self):
        """Verify meta tags in templates"""
        
        print("\n🏷️ Checking meta tags...")
        print("=" * 50)
        
        # Read the social previews template
        template_path = 'templates/partials/_social_previews.html'
        if os.path.exists(template_path):
            with open(template_path, 'r') as f:
                content = f.read()
                
                # Check for essential meta tags
                essential_tags = [
                    ('og:image', r'<meta property="og:image"'),
                    ('og:title', r'<meta property="og:title"'),
                    ('og:description', r'<meta property="og:description"'),
                    ('twitter:card', r'<meta name="twitter:card"'),
                    ('twitter:image', r'<meta name="twitter:image"'),
                ]
                
                for tag_name, pattern in essential_tags:
                    if re.search(pattern, content):
                        self.success.append(f"✅ Found {tag_name} meta tag")
                    else:
                        self.errors.append(f"❌ Missing {tag_name} meta tag")
                
                # Check for image URLs
                if 'seo-preview-1200x630.jpg' in content:
                    self.success.append("✅ Social preview image referenced in template")
                else:
                    self.warnings.append("⚠️ seo-preview-1200x630.jpg not referenced in template")
    
    def generate_test_urls(self):
        """Generate test URLs for validation"""
        
        print("\n🔗 Test URLs for validation...")
        print("=" * 50)
        
        test_urls = [
            f"{self.domain}/",
            f"{self.domain}/services/forensic-economics/",
            f"{self.domain}/locations/",
            f"{self.domain}/contact/",
        ]
        
        print("\nTest these URLs with online validators:")
        print("-" * 40)
        
        for url in test_urls:
            print(f"\n📍 {url}")
            print(f"   Facebook: https://developers.facebook.com/tools/debug/?q={url}")
            print(f"   Twitter: https://cards-dev.twitter.com/validator")
            print(f"   LinkedIn: https://www.linkedin.com/post-inspector/inspect/{url}")
    
    def generate_preview_test_html(self):
        """Generate a test HTML file to verify previews locally"""
        
        test_html = """<!DOCTYPE html>
<html>
<head>
    <title>Social Preview Test - Skerritt Economics</title>
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://skerritteconomics.com/">
    <meta property="og:title" content="Skerritt Economics & Consulting - Expert Forensic Economics">
    <meta property="og:description" content="Premier forensic economics firm providing expert witness services. Economic damage calculations, business valuations, and life care planning. Free consultation: (203) 605-2814">
    <meta property="og:image" content="https://skerritteconomics.com/static/images/seo-preview-1200x630.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://skerritteconomics.com/">
    <meta name="twitter:title" content="Skerritt Economics & Consulting">
    <meta name="twitter:description" content="Expert forensic economics and business valuation services for litigation support across all 50 states.">
    <meta name="twitter:image" content="https://skerritteconomics.com/static/images/seo-preview-1200x630.jpg">
    
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; max-width: 800px; margin: 0 auto; }
        .preview { border: 1px solid #ddd; padding: 15px; margin: 20px 0; border-radius: 8px; }
        .preview h3 { margin-top: 0; color: #2c3e50; }
        .preview img { max-width: 100%; height: auto; border: 1px solid #eee; }
        .test-link { display: inline-block; padding: 10px 20px; background: #2c3e50; color: white; text-decoration: none; border-radius: 5px; margin: 10px 10px 10px 0; }
        .test-link:hover { background: #34495e; }
    </style>
</head>
<body>
    <h1>Social Media Preview Test</h1>
    
    <div class="preview">
        <h3>How your link will appear:</h3>
        <img src="static/images/seo-preview-1200x630.jpg" alt="Preview">
        <h4>Skerritt Economics & Consulting</h4>
        <p>Premier forensic economics firm providing expert witness services. Economic damage calculations, business valuations, and life care planning.</p>
        <small>skerritteconomics.com</small>
    </div>
    
    <h2>Test Your Previews:</h2>
    <p>Share this page URL to test how it appears in:</p>
    <ul>
        <li>Text messages (iMessage, SMS)</li>
        <li>WhatsApp</li>
        <li>Facebook Messenger</li>
        <li>Slack</li>
        <li>Email clients</li>
    </ul>
    
    <h2>Validation Tools:</h2>
    <a href="https://developers.facebook.com/tools/debug/" class="test-link" target="_blank">Facebook Debugger</a>
    <a href="https://cards-dev.twitter.com/validator" class="test-link" target="_blank">Twitter Card Validator</a>
    <a href="https://www.linkedin.com/post-inspector/" class="test-link" target="_blank">LinkedIn Inspector</a>
    <a href="https://metatags.io/" class="test-link" target="_blank">Meta Tags Preview Tool</a>
</body>
</html>"""
        
        with open('social_preview_test.html', 'w') as f:
            f.write(test_html)
        
        self.success.append("✅ Created social_preview_test.html for local testing")
    
    def print_report(self):
        """Print verification report"""
        
        print("\n" + "=" * 50)
        print("📊 VERIFICATION REPORT")
        print("=" * 50)
        
        if self.success:
            print("\n✅ SUCCESS:")
            for item in self.success:
                print(f"   {item}")
        
        if self.warnings:
            print("\n⚠️ WARNINGS:")
            for item in self.warnings:
                print(f"   {item}")
        
        if self.errors:
            print("\n❌ ERRORS TO FIX:")
            for item in self.errors:
                print(f"   {item}")
        else:
            print("\n🎉 No errors found! Your social previews are properly configured.")
        
        print("\n" + "=" * 50)
        print("📱 NEXT STEPS:")
        print("=" * 50)
        print("""
1. Test a link by sending it via iMessage or WhatsApp
   - The preview should show your 1200x630 image
   
2. Clear cache on social platforms:
   - Facebook: Use the debugger tool to scrape again
   - LinkedIn: Use the post inspector to refresh
   
3. For production site:
   - Deploy these changes
   - Test with actual domain URLs
   - Monitor with Google Search Console
   
4. Important files to keep updated:
   - /static/images/seo-preview-1200x630.jpg (main preview)
   - /static/images/SEC_LOGO.png (logo)
   - /templates/partials/_social_previews.html (meta tags)
""")


def main():
    """Run verification"""
    
    print("\n🚀 Social Media Preview Verification Tool")
    print("=" * 50)
    
    verifier = SocialPreviewVerifier()
    
    # Run all checks
    verifier.verify_local_setup()
    verifier.verify_meta_tags()
    verifier.generate_test_urls()
    verifier.generate_preview_test_html()
    
    # Print report
    verifier.print_report()
    
    print("\n💡 TIP: Open social_preview_test.html in your browser to see a preview")
    print("        of how your links will appear when shared.\n")


if __name__ == '__main__':
    main()