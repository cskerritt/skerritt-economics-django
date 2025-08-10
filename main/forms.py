from django import forms
from .models import ContactInquiry

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