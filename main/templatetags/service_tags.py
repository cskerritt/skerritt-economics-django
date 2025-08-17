"""
Template tags for service-related functionality
"""

from django import template
from ..utils import get_services_config

register = template.Library()

@register.simple_tag
def get_services():
    """
    Template tag to get services configuration.
    Usage: {% get_services as services %}
    """
    return get_services_config()

@register.inclusion_tag('main/includes/service_list.html')
def render_service_list(location_context="legal proceedings", 
                        location_phrase="", 
                        case_context="injury cases",
                        disability_context="disability cases"):
    """
    Inclusion tag to render the service list with context.
    Usage: {% render_service_list location_context="Texas courts" %}
    """
    return {
        'services_config': get_services_config(),
        'location_context': location_context,
        'location_phrase': location_phrase,
        'case_context': case_context,
        'disability_context': disability_context
    }