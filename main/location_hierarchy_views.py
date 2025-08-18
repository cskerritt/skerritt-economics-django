"""
Views for location hierarchy pages (/locations/states/ and /locations/cities/)
"""

from django.views.generic import TemplateView

class StateLocationView(TemplateView):
    """View for state location pages under /locations/states/"""
    template_name = "main/locations/state.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["state_slug"] = kwargs.get("state_slug", "")
        context["state_name"] = kwargs.get("state_name", "")
        context["state_abbr"] = kwargs.get("state_abbr", "")
        context["page_title"] = f"Economic Expert Services in {context["state_name"]}"
        context["meta_description"] = f"Professional forensic economics, business valuation, and expert witness services throughout {context["state_name"]}."
        return context

class CityLocationView(TemplateView):
    """View for city location pages under /locations/cities/"""
    template_name = "main/locations/city.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["city_slug"] = kwargs.get("city_slug", "")
        context["city_name"] = kwargs.get("city_name", "")
        context["state_name"] = kwargs.get("state_name", "")
        context["state_slug"] = kwargs.get("state_slug", "")
        context["page_title"] = f"Economic Expert Services in {context["city_name"]}, {context["state_name"]}"
        context["meta_description"] = f"Expert economic analysis and testimony services in {context["city_name"]}, {context["state_name"]}. Forensic economics, business valuation, and more."
        return context

class CityServiceLocationView(TemplateView):
    """View for service-specific city location pages"""
    template_name = "main/locations/city_service.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["city_slug"] = kwargs.get("city_slug", "")
        context["city_name"] = kwargs.get("city_name", "")
        context["state_name"] = kwargs.get("state_name", "")
        context["state_slug"] = kwargs.get("state_slug", "")
        context["service_slug"] = kwargs.get("service_slug", "")
        context["service_name"] = kwargs.get("service_name", "")
        context["page_title"] = f"{context["service_name"]} in {context["city_name"]}, {context["state_name"]}"
        context["meta_description"] = f"Professional {context["service_name"].lower()} services in {context["city_name"]}, {context["state_name"]}. Expert testimony and analysis."
        return context