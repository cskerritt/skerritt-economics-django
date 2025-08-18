"""
Template filters for service rendering
"""

from django import template

register = template.Library()

@register.filter
def format_suffix(suffix_template, context):
    """
    Format a service suffix template with context variables.
    
    Usage: {{ service.suffix_template|format_suffix:suffix_context }}
    """
    if not suffix_template or not context:
        return ''
    
    try:
        # Simple string formatting with the context dictionary
        return ' ' + suffix_template.format(**context) + '.'
    except (KeyError, ValueError):
        # If formatting fails, return empty string
        return '.'