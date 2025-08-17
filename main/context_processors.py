"""
Context processors to make common data available to all templates
"""

from .utils import get_services_config

def services_config(request):
    """
    Add services configuration to template context.
    This makes the services list available to all templates.
    """
    return {
        'services_config': get_services_config()
    }