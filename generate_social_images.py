#!/usr/bin/env python3
"""
Generate Social Media Preview Images
Creates all necessary image sizes for optimal social media sharing
"""

import os
from PIL import Image, ImageDraw, ImageFont
import json


class SocialImageGenerator:
    """Generate social media preview images in all required sizes"""
    
    def __init__(self, logo_path='static/images/SEC_LOGO.png'):
        self.logo_path = logo_path
        self.output_dir = 'static/images'
        self.brand_color = '#2c3e50'
        self.accent_color = '#e74c3c'
        self.text_color = '#333333'
        self.bg_color = '#f8f9fa'
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_all_images(self):
        """Generate all required image sizes"""
        
        # Social media preview sizes
        sizes = {
            # Open Graph (Facebook, LinkedIn, WhatsApp)
            'seo-preview-1200x630': (1200, 630),
            'seo-preview-square-1200x1200': (1200, 1200),
            
            # Twitter
            'twitter-card-1200x600': (1200, 600),
            'twitter-summary-480x480': (480, 480),
            
            # Apple Touch Icons
            'apple-icon-57x57': (57, 57),
            'apple-icon-60x60': (60, 60),
            'apple-icon-72x72': (72, 72),
            'apple-icon-76x76': (76, 76),
            'apple-icon-114x114': (114, 114),
            'apple-icon-120x120': (120, 120),
            'apple-icon-144x144': (144, 144),
            'apple-icon-152x152': (152, 152),
            'apple-icon-180x180': (180, 180),
            
            # Android Icons
            'android-icon-36x36': (36, 36),
            'android-icon-48x48': (48, 48),
            'android-icon-72x72': (72, 72),
            'android-icon-96x96': (96, 96),
            'android-icon-144x144': (144, 144),
            'android-icon-192x192': (192, 192),
            'android-icon-512x512': (512, 512),
            
            # Microsoft Tiles
            'ms-icon-70x70': (70, 70),
            'ms-icon-144x144': (144, 144),
            'ms-icon-150x150': (150, 150),
            'ms-icon-310x150': (310, 150),
            'ms-icon-310x310': (310, 310),
            
            # Favicons
            'favicon-16x16': (16, 16),
            'favicon-32x32': (32, 32),
            'favicon-96x96': (96, 96),
            'favicon-192x192': (192, 192),
        }
        
        for filename, size in sizes.items():
            self.create_image(filename, size)
        
        print(f"Generated {len(sizes)} social media preview images")
    
    def create_image(self, filename, size):
        """Create a single image with logo and branding"""
        
        width, height = size
        
        # Create new image with brand colors
        img = Image.new('RGB', (width, height), self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Add gradient background for larger images
        if width >= 600:
            self.add_gradient(draw, width, height)
        
        # Add logo and text for larger images
        if width >= 200:
            self.add_logo_and_text(img, draw, width, height)
        else:
            # For small icons, just use a simplified version
            self.add_simple_icon(draw, width, height)
        
        # Save the image
        output_path = os.path.join(self.output_dir, f'{filename}.jpg')
        img.save(output_path, 'JPEG', quality=95)
        print(f"Created: {output_path}")
    
    def add_gradient(self, draw, width, height):
        """Add a gradient background"""
        for i in range(height):
            # Calculate gradient color
            ratio = i / height
            r = int(44 + (248 - 44) * ratio)  # From brand color to white
            g = int(62 + (249 - 62) * ratio)
            b = int(80 + (250 - 80) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            draw.line([(0, i), (width, i)], fill=color)
    
    def add_logo_and_text(self, img, draw, width, height):
        """Add logo and company text to image"""
        
        # Try to load the actual logo
        try:
            logo = Image.open(self.logo_path)
            # Resize logo to fit
            logo_width = min(width * 0.6, 400)
            logo_height = int(logo_width * logo.height / logo.width)
            if logo_height > height * 0.3:
                logo_height = int(height * 0.3)
                logo_width = int(logo_height * logo.width / logo.height)
            
            logo = logo.resize((int(logo_width), int(logo_height)), Image.Resampling.LANCZOS)
            
            # Position logo
            logo_x = (width - logo_width) // 2
            logo_y = height // 4
            
            img.paste(logo, (int(logo_x), int(logo_y)), logo if logo.mode == 'RGBA' else None)
        except:
            # If logo doesn't exist, create text placeholder
            self.add_text_logo(draw, width, height)
        
        # Add tagline for larger images
        if width >= 600:
            try:
                # Try to use a nice font
                font_size = min(width // 30, 24)
                font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
            except:
                font = ImageFont.load_default()
            
            tagline = "Expert Forensic Economics & Business Valuation"
            text_bbox = draw.textbbox((0, 0), tagline, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_x = (width - text_width) // 2
            text_y = height * 0.6
            
            draw.text((text_x, text_y), tagline, fill=self.text_color, font=font)
            
            # Add contact info
            contact = "Free Consultation: (203) 605-2814"
            contact_bbox = draw.textbbox((0, 0), contact, font=font)
            contact_width = contact_bbox[2] - contact_bbox[0]
            contact_x = (width - contact_width) // 2
            contact_y = height * 0.7
            
            draw.text((contact_x, contact_y), contact, fill=self.accent_color, font=font)
    
    def add_text_logo(self, draw, width, height):
        """Add text-based logo if image not available"""
        try:
            font_size = min(width // 15, 48)
            font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
        except:
            font = ImageFont.load_default()
        
        text = "SKERRITT\nECONOMICS"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 3
        
        draw.text((text_x, text_y), text, fill=self.brand_color, font=font, align='center')
    
    def add_simple_icon(self, draw, width, height):
        """Add simple icon for small sizes"""
        # Draw a simple "SE" monogram
        try:
            font_size = min(width // 2, height // 2)
            font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
        except:
            font = ImageFont.load_default()
        
        text = "SE"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        
        # Draw background circle for icon
        padding = min(width, height) // 10
        draw.ellipse([padding, padding, width-padding, height-padding], 
                    fill=self.brand_color)
        
        # Draw text
        draw.text((text_x, text_y), text, fill='white', font=font)
    
    def create_favicon_ico(self):
        """Create a multi-resolution favicon.ico file"""
        sizes = [(16, 16), (32, 32), (48, 48)]
        images = []
        
        for size in sizes:
            img = Image.new('RGB', size, self.bg_color)
            draw = ImageDraw.Draw(img)
            self.add_simple_icon(draw, size[0], size[1])
            images.append(img)
        
        # Save as ICO
        output_path = os.path.join(self.output_dir, 'favicon.ico')
        images[0].save(output_path, format='ICO', sizes=sizes)
        print(f"Created: {output_path}")


def main():
    """Generate all social media images"""
    
    print("Generating social media preview images...")
    print("=" * 50)
    
    generator = SocialImageGenerator()
    
    # Generate all images
    generator.generate_all_images()
    
    # Create favicon.ico
    generator.create_favicon_ico()
    
    print("=" * 50)
    print("✅ All social media images generated successfully!")
    print("\nIMPORTANT: Replace the generated placeholder images with your actual branded images:")
    print("1. seo-preview-1200x630.jpg - Main social sharing image")
    print("2. seo-preview-square-1200x1200.jpg - Square format for some platforms")
    print("3. SEC_LOGO.png - Your actual logo file")
    print("\nThese images will now appear when sharing links via:")
    print("- Text messages (iMessage, SMS)")
    print("- WhatsApp")
    print("- Facebook")
    print("- LinkedIn")
    print("- Twitter")
    print("- Email clients")


if __name__ == '__main__':
    main()