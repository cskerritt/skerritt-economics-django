from django import forms
from .models import ContactInquiry, Referral

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'organization', 'case_type', 
                 'jurisdiction', 'timeline', 'case_details']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(555) 123-4567',
                'required': True
            }),
            'organization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Law Firm or Organization'
            }),
            'case_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'jurisdiction': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'timeline': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'case_details': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Please provide a brief description of your case and how we can assist you...',
                'required': True
            })
        }
        labels = {
            'name': 'Full Name *',
            'email': 'Email Address *',
            'phone': 'Phone Number *',
            'organization': 'Law Firm / Organization',
            'case_type': 'Case Type *',
            'jurisdiction': 'Jurisdiction *',
            'timeline': 'Timeline *',
            'case_details': 'Case Details *'
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Basic phone validation - remove non-digits and check length
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError("Please enter a valid phone number with at least 10 digits.")
        return phone


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = [
            'referrer_name', 'referrer_email', 'referrer_phone', 'referrer_firm',
            'referrer_title', 'referrer_location', 'referral_type', 'case_type',
            'case_caption', 'court_jurisdiction', 'case_number', 'expert_needed_for',
            'opposing_expert', 'urgency', 'trial_date', 'discovery_deadline',
            'damages_estimate', 'case_description', 'specific_requirements',
            'preferred_contact_method', 'best_time_to_contact'
        ]
        widgets = {
            'referrer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True
            }),
            'referrer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
                'required': True
            }),
            'referrer_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(555) 123-4567',
                'required': True
            }),
            'referrer_firm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Law Firm or Company Name'
            }),
            'referrer_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Partner, Associate, Paralegal'
            }),
            'referrer_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, State',
                'required': True
            }),
            'referral_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'case_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'case_caption': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Smith v. Jones'
            }),
            'court_jurisdiction': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Superior Court of Rhode Island'
            }),
            'case_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Case/Docket Number'
            }),
            'expert_needed_for': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe the expert services needed (e.g., lost earnings analysis, business valuation, life care planning)',
                'required': True
            }),
            'opposing_expert': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of opposing expert if known'
            }),
            'urgency': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'trial_date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'MM/DD/YYYY or TBD'
            }),
            'discovery_deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'MM/DD/YYYY or TBD'
            }),
            'damages_estimate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., $100,000 - $500,000'
            }),
            'case_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Provide a brief description of the case facts and economic issues involved',
                'required': True
            }),
            'specific_requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any specific requirements, preferences, or additional information'
            }),
            'preferred_contact_method': forms.Select(attrs={
                'class': 'form-control'
            }),
            'best_time_to_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Weekdays 9am-5pm EST'
            })
        }
        labels = {
            'referrer_name': 'Your Name *',
            'referrer_email': 'Your Email *',
            'referrer_phone': 'Your Phone *',
            'referrer_firm': 'Firm/Organization',
            'referrer_title': 'Your Title',
            'referrer_location': 'Your Location *',
            'referral_type': 'Referral Type *',
            'case_type': 'Case Type *',
            'case_caption': 'Case Caption',
            'court_jurisdiction': 'Court/Jurisdiction',
            'case_number': 'Case Number',
            'expert_needed_for': 'Expert Services Needed *',
            'opposing_expert': 'Opposing Expert',
            'urgency': 'Urgency *',
            'trial_date': 'Trial/Arbitration Date',
            'discovery_deadline': 'Discovery Deadline',
            'damages_estimate': 'Estimated Damages',
            'case_description': 'Case Description *',
            'specific_requirements': 'Additional Requirements',
            'preferred_contact_method': 'Preferred Contact Method',
            'best_time_to_contact': 'Best Time to Contact'
        }