from django.core.management.base import BaseCommand
from PIL import Image
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Optimize images and generate WebP versions'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            default='static/images',
            help='Path to images directory'
        )

    def handle(self, *args, **options):
        images_path = Path(options['path'])
        
        if not images_path.exists():
            self.stdout.write(self.style.ERROR(f"Path {images_path} does not exist"))
            return
        
        # Process all images
        image_extensions = ['.jpg', '.jpeg', '.png']
        processed = 0
        
        for ext in image_extensions:
            for image_file in images_path.glob(f'**/*{ext}'):
                try:
                    self.optimize_image(image_file)
                    processed += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing {image_file}: {e}"))
        
        self.stdout.write(self.style.SUCCESS(f"Successfully optimized {processed} images"))

    def optimize_image(self, image_path):
        """Optimize a single image and create WebP version"""
        img = Image.open(image_path)
        
        # Convert RGBA to RGB if necessary
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Save optimized original
        img.save(image_path, optimize=True, quality=85)
        
        # Create WebP version
        webp_path = image_path.with_suffix('.webp')
        img.save(webp_path, 'WEBP', optimize=True, quality=85)
        
        # Create responsive sizes
        sizes = [320, 640, 768, 1024, 1280, 1920]
        for size in sizes:
            if img.width > size:
                # Calculate proportional height
                ratio = size / img.width
                new_height = int(img.height * ratio)
                
                # Resize image
                resized = img.resize((size, new_height), Image.Resampling.LANCZOS)
                
                # Save resized versions
                base_path = image_path.stem
                parent_dir = image_path.parent
                
                # Save regular format
                resized_path = parent_dir / f"{base_path}-{size}w{image_path.suffix}"
                resized.save(resized_path, optimize=True, quality=85)
                
                # Save WebP format
                webp_resized_path = parent_dir / f"{base_path}-{size}w.webp"
                resized.save(webp_resized_path, 'WEBP', optimize=True, quality=85)
        
        self.stdout.write(self.style.SUCCESS(f"Optimized: {image_path}"))