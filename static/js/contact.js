// Contact form enhancement
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form');
    
    if (form) {
        // Add real-time validation
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
        
        // Validate individual field
        function validateField(field) {
            const value = field.value.trim();
            const isRequired = field.hasAttribute('required');
            
            // Remove previous error
            field.classList.remove('is-invalid');
            const errorDiv = field.parentElement.querySelector('.error-message');
            if (errorDiv && !errorDiv.classList.contains('text-danger')) {
                errorDiv.remove();
            }
            
            // Check if required field is empty
            if (isRequired && !value) {
                showError(field, 'This field is required');
                return false;
            }
            
            // Email validation
            if (field.type === 'email' && value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    showError(field, 'Please enter a valid email address');
                    return false;
                }
            }
            
            // Phone validation
            if (field.type === 'tel' && value) {
                const phoneDigits = value.replace(/\D/g, '');
                if (phoneDigits.length < 10) {
                    showError(field, 'Please enter a valid phone number');
                    return false;
                }
            }
            
            field.classList.add('is-valid');
            return true;
        }
        
        // Show error message
        function showError(field, message) {
            field.classList.add('is-invalid');
            
            // Check if error message already exists
            let errorDiv = field.parentElement.querySelector('.error-message:not(.text-danger)');
            if (!errorDiv) {
                errorDiv = document.createElement('div');
                errorDiv.className = 'error-message text-danger small mt-1';
                field.parentElement.appendChild(errorDiv);
            }
            errorDiv.textContent = message;
        }
    }
});