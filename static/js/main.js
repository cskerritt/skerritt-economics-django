// Main JavaScript file for Skerritt Economics & Consulting

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavigation();
    initTracking();
    initFormValidation();
});

// Navigation functionality
function initNavigation() {
    // Mobile menu toggle (if needed)
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.navbar-menu');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Dropdown menu accessibility
    const dropdowns = document.querySelectorAll('.has-dropdown');
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('a');
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    });
}

// Tracking functions (Google Analytics placeholders)
function trackFormSubmission(formName) {
    // Google Analytics event tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', 'form_submit', {
            'form_name': formName
        });
    }
    console.log('Form submitted:', formName);
}

function trackPhoneClick() {
    // Track phone number clicks
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            'event_category': 'contact',
            'event_label': 'phone'
        });
    }
    console.log('Phone number clicked');
}

function trackEmailClick() {
    // Track email clicks
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            'event_category': 'contact',
            'event_label': 'email'
        });
    }
    console.log('Email clicked');
}

// Initialize tracking
function initTracking() {
    // Add tracking to email links
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
    emailLinks.forEach(link => {
        link.addEventListener('click', trackEmailClick);
    });
}

// Form validation
function initFormValidation() {
    const forms = document.querySelectorAll('form.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!validateForm(form)) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

function validateForm(form) {
    let isValid = true;
    
    // Validate required fields
    const requiredFields = form.querySelectorAll('[required]');
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            showFieldError(field, 'This field is required');
        } else {
            clearFieldError(field);
        }
    });
    
    // Validate email fields
    const emailFields = form.querySelectorAll('[type="email"]');
    emailFields.forEach(field => {
        if (field.value && !isValidEmail(field.value)) {
            isValid = false;
            showFieldError(field, 'Please enter a valid email address');
        }
    });
    
    // Validate phone fields
    const phoneFields = form.querySelectorAll('[type="tel"]');
    phoneFields.forEach(field => {
        if (field.value && !isValidPhone(field.value)) {
            isValid = false;
            showFieldError(field, 'Please enter a valid phone number');
        }
    });
    
    return isValid;
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function isValidPhone(phone) {
    const re = /^[\d\s\-\(\)\+]+$/;
    return re.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

function showFieldError(field, message) {
    const errorDiv = field.parentElement.querySelector('.error-message') || createErrorDiv();
    errorDiv.textContent = message;
    field.parentElement.appendChild(errorDiv);
    field.classList.add('is-invalid');
}

function clearFieldError(field) {
    const errorDiv = field.parentElement.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
    field.classList.remove('is-invalid');
}

function createErrorDiv() {
    const div = document.createElement('div');
    div.className = 'error-message text-danger small mt-1';
    return div;
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Calculator helper functions (will be extended by individual tool scripts)
window.CalculatorUtils = {
    formatCurrency: function(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(amount);
    },
    
    formatNumber: function(num) {
        return new Intl.NumberFormat('en-US').format(num);
    },
    
    calculatePresentValue: function(futureValue, rate, periods) {
        return futureValue / Math.pow(1 + rate, periods);
    },
    
    calculateFutureValue: function(presentValue, rate, periods) {
        return presentValue * Math.pow(1 + rate, periods);
    }
};

// Export functions for use in other scripts
window.SEC = {
    trackFormSubmission,
    trackPhoneClick,
    trackEmailClick,
    validateForm,
    CalculatorUtils: window.CalculatorUtils
};