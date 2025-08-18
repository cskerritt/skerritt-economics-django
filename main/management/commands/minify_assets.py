from django.core.management.base import BaseCommand
from pathlib import Path
import re

class Command(BaseCommand):
    help = "Minify CSS and JavaScript files for production"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="static",
            help="Path to static directory"
        )

    def handle(self, *args, **options):
        static_path = Path(options["path"])
        
        if not static_path.exists():
            self.stdout.write(self.style.ERROR(f"Path {static_path} does not exist"))
            return
        
        # Minify CSS files
        css_files = list(static_path.glob("**/*.css"))
        for css_file in css_files:
            if ".min." not in css_file.name:
                self.minify_css(css_file)
        
        # Minify JS files
        js_files = list(static_path.glob("**/*.js"))
        for js_file in js_files:
            if ".min." not in js_file.name:
                self.minify_js(js_file)
        
        self.stdout.write(self.style.SUCCESS(f"Minified {len(css_files)} CSS and {len(js_files)} JS files"))

    def minify_css(self, file_path):
        """Simple CSS minification"""
        with open(file_path, "r") as f:
            css = f.read()
        
        # Remove comments
        css = re.sub(r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", css)
        
        # Remove unnecessary whitespace
        css = re.sub(r"\s+", " ", css)
        css = re.sub(r":\s+", ":", css)
        css = re.sub(r";\s+", ";", css)
        css = re.sub(r"\s*{\s*", "{", css)
        css = re.sub(r"\s*}\s*", "}", css)
        css = re.sub(r"\s*,\s*", ",", css)
        
        # Remove last semicolon before closing brace
        css = re.sub(r";}", "}", css)
        
        # Save minified version
        min_path = file_path.parent / f"{file_path.stem}.min.css"
        with open(min_path, "w") as f:
            f.write(css.strip())
        
        self.stdout.write(f"Minified: {file_path} -> {min_path}")

    def minify_js(self, file_path):
        """Simple JavaScript minification"""
        with open(file_path, "r") as f:
            js = f.read()
        
        # Remove single-line comments (but keep URLs)
        js = re.sub(r"(?<!:)//[^\n]*", "", js)
        
        # Remove multi-line comments
        js = re.sub(r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", js)
        
        # Remove unnecessary whitespace
        js = re.sub(r"\s+", " ", js)
        js = re.sub(r"\s*([=+\-*/{}();,:])\s*", r"\1", js)
        
        # Remove trailing semicolons before closing braces
        js = re.sub(r";}", "}", js)
        
        # Save minified version
        min_path = file_path.parent / f"{file_path.stem}.min.js"
        with open(min_path, "w") as f:
            f.write(js.strip())
        
        self.stdout.write(f"Minified: {file_path} -> {min_path}")