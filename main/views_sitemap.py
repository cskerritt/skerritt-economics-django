from django.contrib.sitemaps import views as sitemap_views
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def sitemap(request, sitemaps, **kwargs):
    """
    Custom sitemap view that forces HTTPS protocol
    """
    # Set the request to appear as HTTPS
    request.META['wsgi.url_scheme'] = 'https'
    if 'HTTP_X_FORWARDED_PROTO' not in request.META:
        request.META['HTTP_X_FORWARDED_PROTO'] = 'https'
    
    # Override is_secure to always return True
    original_is_secure = request.is_secure
    request.is_secure = lambda: True
    
    try:
        # Get the response from the default sitemap view
        response = sitemap_views.sitemap(request, sitemaps, **kwargs)
        
        # Ensure the content uses HTTPS
        if hasattr(response, 'content'):
            content = response.content.decode('utf-8')
            # Replace all HTTP URLs with HTTPS
            content = content.replace('http://skerritteconomics.com', 'https://skerritteconomics.com')
            content = content.replace('http://www.skerritteconomics.com', 'https://www.skerritteconomics.com')
            response.content = content.encode('utf-8')
        
        return response
    finally:
        # Restore original is_secure method
        request.is_secure = original_is_secure