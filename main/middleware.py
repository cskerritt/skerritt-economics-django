"""
Custom middleware for performance optimization
"""
from django.utils.cache import add_never_cache_headers, patch_cache_control
from django.conf import settings
import re

class CacheControlMiddleware:
    """
    Add cache control headers for static assets
    """
    def __init__(self, get_response):
        self.get_response = get_response
        
        # Define cache patterns
        self.cache_patterns = [
            (r'\.(jpg|jpeg|png|gif|webp|svg|ico)$', 86400 * 30),  # Images: 30 days
            (r'\.(css|js)$', 86400 * 7),  # CSS/JS: 7 days
            (r'\.(woff|woff2|ttf|eot)$', 86400 * 30),  # Fonts: 30 days
        ]

    def __call__(self, request):
        response = self.get_response(request)
        
        # Only apply in production
        if not settings.DEBUG:
            path = request.path.lower()
            
            # Check if path matches any cache pattern
            for pattern, max_age in self.cache_patterns:
                if re.search(pattern, path):
                    patch_cache_control(
                        response,
                        max_age=max_age,
                        public=True,
                        immutable=True
                    )
                    break
            else:
                # For HTML pages, set shorter cache
                if response.get('Content-Type', '').startswith('text/html'):
                    patch_cache_control(
                        response,
                        max_age=3600,  # 1 hour
                        must_revalidate=True,
                        stale_while_revalidate=86400
                    )
        
        return response

class SecurityHeadersMiddleware:
    """
    Add security headers to responses
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Add security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # Add CSP header (adjust based on your needs)
        csp = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://www.googletagmanager.com https://www.google-analytics.com",
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com",
            "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com",
            "img-src 'self' data: https:",
            "connect-src 'self' https://www.google-analytics.com",
        ]
        response['Content-Security-Policy'] = '; '.join(csp)
        
        # Add Feature Policy
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        
        return response

class CompressionMiddleware:
    """
    Enable compression for text-based responses
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if response is text-based and large enough to compress
        content_type = response.get('Content-Type', '')
        compressible_types = ['text/', 'application/json', 'application/javascript', 'application/xml']
        
        if any(ct in content_type for ct in compressible_types):
            if len(response.content) > 1024:  # Only compress if > 1KB
                response['Vary'] = 'Accept-Encoding'
        
        return response