from django.db import models
from django.utils import timezone

class ContactInquiry(models.Model):
    CASE_TYPE_CHOICES = [
        ("personal_injury", "Personal Injury"),
        ("wrongful_death", "Wrongful Death"),
        ("medical_malpractice", "Medical Malpractice"),
        ("employment", "Employment Litigation"),
        ("business_valuation", "Business Valuation"),
        ("commercial_dispute", "Commercial Dispute"),
        ("other", "Other"),
    ]
    
    JURISDICTION_CHOICES = [
        ("state_court", "State Court"),
        ("federal_court", "Federal Court"),
        ("arbitration", "Arbitration"),
        ("mediation", "Mediation"),
        ("administrative", "Administrative"),
        ("other", "Other"),
    ]
    
    TIMELINE_CHOICES = [
        ("immediate", "Immediate (< 30 days)"),
        ("soon", "Soon (1-3 months)"),
        ("planning", "Planning (3-6 months)"),
        ("future", "Future (> 6 months)"),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organization = models.CharField(max_length=200, blank=True)
    
    case_type = models.CharField(max_length=50, choices=CASE_TYPE_CHOICES)
    jurisdiction = models.CharField(max_length=50, choices=JURISDICTION_CHOICES)
    timeline = models.CharField(max_length=50, choices=TIMELINE_CHOICES)
    
    case_details = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    responded = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="Internal notes")
    
    class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ["-created_date"]
    
    def __str__(self):
        return f"{self.name} - {self.get_case_type_display()} ({self.created_date.strftime("%Y-%m-%d")})"


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True, help_text="e.g., 'Managing Partner, Smith & Associates'")
    content = models.TextField()
    featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["display_order", "-created_date"]
    
    def __str__(self):
        return f"{self.author} - {self.title}"


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    display_order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["display_order", "question"]
    
    def __str__(self):
        return self.question


class Referral(models.Model):
    REFERRAL_TYPE_CHOICES = [
        ("attorney_to_expert", "Attorney Seeking Expert"),
        ("attorney_to_attorney", "Attorney to Attorney"),
        ("client_needs_expert", "Client Needs Expert"),
        ("expert_collaboration", "Expert Collaboration"),
        ("other", "Other"),
    ]
    
    CASE_TYPE_CHOICES = [
        ("personal_injury", "Personal Injury"),
        ("wrongful_death", "Wrongful Death"),
        ("medical_malpractice", "Medical Malpractice"),
        ("employment", "Employment Litigation"),
        ("business_valuation", "Business Valuation"),
        ("commercial_dispute", "Commercial Dispute"),
        ("divorce", "Divorce/Family Law"),
        ("insurance", "Insurance Dispute"),
        ("construction", "Construction Defect"),
        ("intellectual_property", "Intellectual Property"),
        ("other", "Other"),
    ]
    
    URGENCY_CHOICES = [
        ("urgent", "Urgent - Need within 1 week"),
        ("soon", "Soon - Need within 1 month"),
        ("planning", "Planning - Need within 3 months"),
        ("exploring", "Exploring options"),
    ]
    
    # Referrer Information
    referrer_name = models.CharField(max_length=100)
    referrer_email = models.EmailField()
    referrer_phone = models.CharField(max_length=20)
    referrer_firm = models.CharField(max_length=200, blank=True)
    referrer_title = models.CharField(max_length=100, blank=True, help_text="e.g., Partner, Associate")
    referrer_location = models.CharField(max_length=100, help_text="City, State")
    
    # Referral Type
    referral_type = models.CharField(max_length=50, choices=REFERRAL_TYPE_CHOICES)
    
    # Case Information
    case_type = models.CharField(max_length=50, choices=CASE_TYPE_CHOICES)
    case_caption = models.CharField(max_length=200, blank=True, help_text="Case name if applicable")
    court_jurisdiction = models.CharField(max_length=200, blank=True)
    case_number = models.CharField(max_length=100, blank=True)
    
    # Expert Needs
    expert_needed_for = models.TextField(help_text="Describe what expert services are needed")
    opposing_expert = models.CharField(max_length=200, blank=True, help_text="Name of opposing expert if known")
    
    # Timeline
    urgency = models.CharField(max_length=50, choices=URGENCY_CHOICES)
    trial_date = models.CharField(max_length=100, blank=True, help_text="Trial/arbitration date if scheduled")
    discovery_deadline = models.CharField(max_length=100, blank=True)
    
    # Additional Information
    damages_estimate = models.CharField(max_length=100, blank=True, help_text="Estimated damages range")
    case_description = models.TextField(help_text="Brief description of the case and economic issues")
    specific_requirements = models.TextField(blank=True, help_text="Any specific requirements or preferences")
    
    # Contact Preference
    preferred_contact_method = models.CharField(
        max_length=20,
        choices=[("email", "Email"), ("phone", "Phone"), ("either", "Either")],
        default="either"
    )
    best_time_to_contact = models.CharField(max_length=100, blank=True)
    
    # Administrative
    created_date = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)
    processed_date = models.DateTimeField(null=True, blank=True)
    internal_notes = models.TextField(blank=True, help_text="Internal notes (not shown to referrer)")
    
    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Expert Referral"
        verbose_name_plural = "Expert Referrals"
    
    def __str__(self):
        return f"{self.referrer_name} - {self.get_case_type_display()} - {self.created_date.strftime("%Y-%m-%d")}"
