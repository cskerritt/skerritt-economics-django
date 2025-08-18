from django import template
from django.utils.safestring import mark_safe
import os

register = template.Library()

@register.simple_tag
def optimized_image(src, alt="", css_class="", loading="lazy", sizes="100vw"):
    """
    Generate an optimized image tag with WebP support and responsive srcset
    
    Usage: {% optimized_image "images/hero.jpg" alt="Hero Image" css_class="hero-img" %}
    """
    # Get file path and extension
    base_path, ext = os.path.splitext(src)
    
    # Generate WebP path
    webp_path = f"{base_path}.webp"
    
    # Generate srcset for different sizes
    sizes_list = [320, 640, 768, 1024, 1280, 1920]
    srcset_items = []
    webp_srcset_items = []
    
    for size in sizes_list:
        srcset_items.append(f"{base_path}-{size}w{ext} {size}w")
        webp_srcset_items.append(f"{base_path}-{size}w.webp {size}w")
    
    srcset = ", ".join(srcset_items)
    webp_srcset = ", ".join(webp_srcset_items)
    
    # Build the picture element with WebP support
    html = f"""
    <picture>
        <source type="image/webp" 
                srcset="{webp_srcset}" 
                sizes="{sizes}">
        <source type="image/{ext[1:]}" 
                srcset="{srcset}" 
                sizes="{sizes}">
        <img src="{src}" 
             alt="{alt}" 
             class="{css_class}" 
             loading="{loading}"
             decoding="async">
    </picture>
    """
    
    return mark_safe(html)

@register.simple_tag
def lazy_image(src, alt="", css_class="", width=None, height=None):
    """
    Generate a lazy-loaded image with placeholder
    
    Usage: {% lazy_image "images/team.jpg" alt="Team Photo" css_class="team-img" %}
    """
    # Create a low-quality placeholder (could be a base64 encoded tiny version)
    placeholder = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1"%3E%3Crect fill="%23f0f0f0"/%3E%3C/svg%3E'
    
    width_attr = f'width="{width}"' if width else ""
    height_attr = f'height="{height}"' if height else ""
    
    html = f"""
    <img src="{placeholder}" 
         data-src="{src}" 
         alt="{alt}" 
         class="{css_class} lazy-load" 
         loading="lazy"
         decoding="async"
         {width_attr}
         {height_attr}>
    """
    
    return mark_safe(html)

@register.simple_tag
def responsive_image(src, alt="", css_class="", breakpoints=None):
    """
    Generate responsive image with art direction
    
    Usage: {% responsive_image "images/hero.jpg" alt="Hero" breakpoints=breakpoints_dict %}
    """
    if not breakpoints:
        breakpoints = {
            "mobile": {"max": 767, "src": f"{src.replace('.jpg', '-mobile.jpg')}"},
            "tablet": {"max": 1023, "src": f"{src.replace('.jpg', '-tablet.jpg')}"},
            "desktop": {"min": 1024, "src": src}
        }
    
    sources = []
    for device, config in breakpoints.items():
        if "max" in config:
            media = f"(max-width: {config['max']}px)"
        else:
            media = f"(min-width: {config['min']}px)"
        
        sources.append(f'<source media="{media}" srcset="{config["src"]}">')
    
    html = f"""
    <picture>
        {"".join(sources)}
        <img src="{src}" alt="{alt}" class="{css_class}" loading="lazy">
    </picture>
    """
    
    return mark_safe(html)