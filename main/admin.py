from django.contrib import admin
from .models import ContactInquiry, Testimonial, FAQ, Referral

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'case_type', 'timeline', 'created_date', 'responded']
    list_filter = ['case_type', 'jurisdiction', 'timeline', 'responded', 'created_date']
    search_fields = ['name', 'email', 'organization', 'case_details']
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'organization')
        }),
        ('Case Information', {
            'fields': ('case_type', 'jurisdiction', 'timeline', 'case_details')
        }),
        ('Admin', {
            'fields': ('created_date', 'responded', 'notes')
        })
    )
    
    def mark_as_responded(self, request, queryset):
        queryset.update(responded=True)
    mark_as_responded.short_description = "Mark selected inquiries as responded"
    
    actions = ['mark_as_responded']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'featured', 'display_order']
    list_filter = ['featured']
    search_fields = ['author', 'title', 'content']
    list_editable = ['featured', 'display_order']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'display_order', 'active']
    list_filter = ['active', 'category']
    search_fields = ['question', 'answer']
    list_editable = ['display_order', 'active']


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referrer_name', 'referrer_firm', 'referral_type', 'case_type', 
                    'urgency', 'created_date', 'processed']
    list_filter = ['referral_type', 'case_type', 'urgency', 'processed', 'created_date']
    search_fields = ['referrer_name', 'referrer_email', 'referrer_firm', 'case_caption', 
                     'case_description', 'expert_needed_for']
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date']
    
    fieldsets = (
        ('Referrer Information', {
            'fields': ('referrer_name', 'referrer_email', 'referrer_phone', 
                      'referrer_firm', 'referrer_title', 'referrer_location')
        }),
        ('Referral Type', {
            'fields': ('referral_type',)
        }),
        ('Case Information', {
            'fields': ('case_type', 'case_caption', 'court_jurisdiction', 'case_number')
        }),
        ('Expert Requirements', {
            'fields': ('expert_needed_for', 'opposing_expert')
        }),
        ('Timeline', {
            'fields': ('urgency', 'trial_date', 'discovery_deadline')
        }),
        ('Case Details', {
            'fields': ('damages_estimate', 'case_description', 'specific_requirements')
        }),
        ('Contact Preferences', {
            'fields': ('preferred_contact_method', 'best_time_to_contact')
        }),
        ('Administrative', {
            'fields': ('created_date', 'processed', 'processed_date', 'internal_notes'),
            'classes': ('collapse',)
        })
    )
    
    def mark_as_processed(self, request, queryset):
        from django.utils import timezone
        queryset.update(processed=True, processed_date=timezone.now())
    mark_as_processed.short_description = "Mark selected referrals as processed"
    
    actions = ['mark_as_processed']
