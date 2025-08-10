from django.contrib import admin
from .models import ContactInquiry, Testimonial, FAQ

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
