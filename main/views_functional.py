"""
Function-based views following CLAUDE.md guidelines.
All views use function-based approach with proper error handling and translation.
"""

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page

from .forms import ContactForm, ReferralForm
from .models import Testimonial, FAQ, Referral
from blog.models import Post, CaseStudy


@require_http_methods(["GET"])
def home_view(request):
    """Home page view with featured content."""
    context = {
        "testimonials": Testimonial.objects.filter(featured=True)[:3],
        "recent_posts": Post.objects.filter(status="published", featured=True).select_related("author")[:3],
        "case_studies": CaseStudy.objects.filter(featured=True)[:3],
        "faqs": FAQ.objects.filter(active=True)[:6],
        "page_title": _("Forensic Economist & Business Valuation Expert"),
        "meta_description": _("Expert forensic economics and business valuation services"),
    }
    return render(request, "main/home.html", context)


# Service Views
@require_http_methods(["GET"])
def forensic_economics_view(request):
    """Forensic economics service page."""
    context = {
        "service_name": _("Forensic Economics"),
        "service_slug": "forensic-economics",
        "service_title": _("Forensic Economist"),
        "service_description": _("Economic damage analysis, lost earnings calculations, and expert witness testimony"),
        "page_title": _("Forensic Economics Services"),
    }
    return render(request, "main/services/forensic_economics.html", context)


@require_http_methods(["GET"])
def business_valuation_view(request):
    """Business valuation service page."""
    context = {
        "service_name": _("Business Valuation"),
        "service_slug": "business-valuation",
        "service_title": _("Business Valuation Expert"),
        "service_description": _("Fair market value analysis, business appraisals, and shareholder dispute valuations"),
        "page_title": _("Business Valuation Services"),
    }
    return render(request, "main/services/business_valuation.html", context)


@require_http_methods(["GET"])
def vocational_expert_view(request):
    """Vocational expert service page."""
    context = {
        "service_name": _("Vocational Expert"),
        "service_slug": "vocational-expert",
        "service_title": _("Vocational Expert"),
        "service_description": _("Employability assessments, earning capacity evaluations, and vocational rehabilitation planning"),
        "page_title": _("Vocational Expert Services"),
    }
    return render(request, "main/services/vocational_expert.html", context)


@require_http_methods(["GET"])
def life_care_planning_view(request):
    """Life care planning service page."""
    context = {
        "service_name": _("Life Care Planning"),
        "service_slug": "life-care-planning",
        "service_title": _("Life Care Planner"),
        "service_description": _("Future medical cost projections, catastrophic injury planning, and assistive technology needs"),
        "page_title": _("Life Care Planning Services"),
    }
    return render(request, "main/services/life_care_planning.html", context)


@require_http_methods(["GET"])
def business_consulting_view(request):
    """Business consulting service page."""
    context = {
        "service_name": _("Business Consulting"),
        "service_slug": "business-consulting",
        "service_title": _("Business Consultant"),
        "service_description": _("Strategic planning, operations improvement, and business transformation services"),
        "page_title": _("Business Consulting Services"),
    }
    return render(request, "main/services/business_consulting.html", context)


# Practice Area Views
@require_http_methods(["GET"])
def personal_injury_view(request):
    """Personal injury practice area page."""
    return render(request, "main/practice_areas/personal_injury.html", {
        "page_title": _("Personal Injury Economic Analysis"),
    })


@require_http_methods(["GET"])
def medical_malpractice_view(request):
    """Medical malpractice practice area page."""
    return render(request, "main/practice_areas/medical_malpractice.html", {
        "page_title": _("Medical Malpractice Economic Analysis"),
    })


@require_http_methods(["GET"])
def employment_litigation_view(request):
    """Employment litigation practice area page."""
    return render(request, "main/practice_areas/employment_litigation.html", {
        "page_title": _("Employment Litigation Economic Analysis"),
    })


@require_http_methods(["GET"])
def commercial_disputes_view(request):
    """Commercial disputes practice area page."""
    return render(request, "main/practice_areas/commercial_disputes.html", {
        "page_title": _("Commercial Disputes Economic Analysis"),
    })


# Other Pages
@require_http_methods(["GET"])
def about_view(request):
    """About page."""
    return render(request, "main/about.html", {
        "page_title": _("About Christopher Skerritt"),
    })


@require_http_methods(["GET"])
def case_studies_view(request):
    """Case studies page."""
    context = {
        "case_studies": CaseStudy.objects.filter(published=True).order_by("-created_date"),
        "page_title": _("Case Studies"),
    }
    return render(request, "main/case_studies.html", context)


@require_http_methods(["GET"])
def resources_view(request):
    """Resources page."""
    return render(request, "main/resources.html", {
        "page_title": _("Resources"),
    })


@require_http_methods(["GET", "POST"])
def contact_view(request):
    """Contact form page using Formspree."""
    return render(request, "main/contact_formspree.html", {
        "page_title": _("Contact Us"),
    })


@require_http_methods(["GET"])
def contact_thank_you_view(request):
    """Contact form thank you page."""
    return render(request, "main/contact_thank_you.html", {
        "page_title": _("Thank You"),
    })


@require_http_methods(["GET", "POST"])
def referral_view(request):
    """Expert referral form page."""
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            # Save the referral
            referral = form.save()
            
            # Send email notification
            try:
                subject = _("New Expert Referral: %(name)s - %(case_type)s") % {
                    "name": referral.referrer_name,
                    "case_type": referral.get_case_type_display()
                }
                
                message = f"""
New expert referral received:

REFERRER INFORMATION:
Name: {referral.referrer_name}
Email: {referral.referrer_email}
Phone: {referral.referrer_phone}
Firm: {referral.referrer_firm}
Title: {referral.referrer_title}
Location: {referral.referrer_location}

REFERRAL TYPE: {referral.get_referral_type_display()}

CASE INFORMATION:
Type: {referral.get_case_type_display()}
Caption: {referral.case_caption}
Court: {referral.court_jurisdiction}
Case #: {referral.case_number}

EXPERT SERVICES NEEDED:
{referral.expert_needed_for}

Opposing Expert: {referral.opposing_expert}

TIMELINE:
Urgency: {referral.get_urgency_display()}
Trial Date: {referral.trial_date}
Discovery Deadline: {referral.discovery_deadline}

DAMAGES ESTIMATE: {referral.damages_estimate}

CASE DESCRIPTION:
{referral.case_description}

ADDITIONAL REQUIREMENTS:
{referral.specific_requirements}

CONTACT PREFERENCE:
Method: {referral.get_preferred_contact_method_display()}
Best Time: {referral.best_time_to_contact}

---
Submitted: {referral.created_date.strftime("%Y-%m-%d %H:%M")}
"""
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    ["chris@skerritteconomics.com"],
                    fail_silently=True,
                )
            except Exception as e:
                # Log error but don't fail the form submission
                print(f"Error sending referral email: {e}")
            
            messages.success(request, _("Thank you for your referral. We will review it and contact you shortly."))
            return redirect("referral_thank_you")
    else:
        form = ReferralForm()
    
    context = {
        "form": form,
        "page_title": _("Expert Referral"),
    }
    return render(request, "main/referral.html", context)


@require_http_methods(["GET"])
def referral_thank_you_view(request):
    """Referral thank you page."""
    return render(request, "main/referral_thank_you.html", {
        "page_title": _("Thank You for Your Referral"),
    })


@require_http_methods(["GET"])
def sitemap_view(request):
    """HTML sitemap page."""
    return render(request, "main/sitemap.html", {
        "page_title": _("Site Map"),
    })


@require_http_methods(["GET"])
def location_view(request, state):
    """Location-specific page for a state."""
    from .us_cities_data import US_STATES
    
    # Convert slug to state abbreviation
    state_lookup = {
        "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR",
        "california": "CA", "colorado": "CO", "connecticut": "CT", "delaware": "DE",
        "florida": "FL", "georgia": "GA", "hawaii": "HI", "idaho": "ID",
        "illinois": "IL", "indiana": "IN", "iowa": "IA", "kansas": "KS",
        "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
        "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
        "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV",
        "new-hampshire": "NH", "new-jersey": "NJ", "new-mexico": "NM", "new-york": "NY",
        "north-carolina": "NC", "north-dakota": "ND", "ohio": "OH", "oklahoma": "OK",
        "oregon": "OR", "pennsylvania": "PA", "rhode-island": "RI", "south-carolina": "SC",
        "south-dakota": "SD", "tennessee": "TN", "texas": "TX", "utah": "UT",
        "vermont": "VT", "virginia": "VA", "washington": "WA", "west-virginia": "WV",
        "wisconsin": "WI", "wyoming": "WY"
    }
    
    state_abbr = state_lookup.get(state, "")
    if state_abbr and state_abbr in US_STATES:
        state_data = US_STATES[state_abbr]
        context = {
            "state": state_data["name"],
            "cities": state_data["cities"][:15],  # Top 15 cities
            "state_info": {
                "name": state_data["name"],
                "cities": state_data["cities"][:15],
                "description": _(
                    "Expert forensic economics and business valuation services throughout %(state)s."
                ) % {"state": state_data["name"]}
            },
            "page_title": _("%(state)s Forensic Economist") % {"state": state_data["name"]},
        }
    else:
        state_name = state.replace("-", " ").title()
        context = {
            "state": state_name,
            "cities": [],
            "state_info": {
                "name": state_name,
                "cities": [],
                "description": _("Expert forensic economics and business valuation services."),
            },
            "page_title": _("%(state)s Forensic Economist") % {"state": state_name},
        }
    
    return render(request, "main/location.html", context)


# Services index page
@require_http_methods(["GET"])
def services_index_view(request):
    """Services index page."""
    return render(request, "main/services/index.html", {
        "page_title": _("Our Services"),
    })


# Practice areas index page
@require_http_methods(["GET"])
def practice_areas_index_view(request):
    """Practice areas index page."""
    return render(request, "main/practice_areas/index.html", {
        "page_title": _("Practice Areas"),
    })


# Locations index page
@require_http_methods(["GET"])
def locations_index_view(request):
    """All locations index page."""
    return render(request, "main/locations/index.html", {
        "page_title": _("Service Areas - All 50 States"),
    })