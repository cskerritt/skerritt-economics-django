from django.db import models
from django.utils import timezone

class ContactInquiry(models.Model):
    CASE_TYPE_CHOICES = [
        ('personal_injury', 'Personal Injury'),
        ('wrongful_death', 'Wrongful Death'),
        ('medical_malpractice', 'Medical Malpractice'),
        ('employment', 'Employment Litigation'),
        ('business_valuation', 'Business Valuation'),
        ('commercial_dispute', 'Commercial Dispute'),
        ('other', 'Other'),
    ]
    
    JURISDICTION_CHOICES = [
        ('state_court', 'State Court'),
        ('federal_court', 'Federal Court'),
        ('arbitration', 'Arbitration'),
        ('mediation', 'Mediation'),
        ('administrative', 'Administrative'),
        ('other', 'Other'),
    ]
    
    TIMELINE_CHOICES = [
        ('immediate', 'Immediate (< 30 days)'),
        ('soon', 'Soon (1-3 months)'),
        ('planning', 'Planning (3-6 months)'),
        ('future', 'Future (> 6 months)'),
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
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.name} - {self.get_case_type_display()} ({self.created_date.strftime('%Y-%m-%d')})"


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True, help_text="e.g., 'Managing Partner, Smith & Associates'")
    content = models.TextField()
    featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['display_order', '-created_date']
    
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
        ordering = ['display_order', 'question']
    
    def __str__(self):
        return self.question
