/**
 * Main JavaScript entry point
 * Initializes HTMX, Alpine.js, and custom functionality
 */

// Import styles
import '../css/main.css';

// Import HTMX and Alpine configurations
import './htmx-config';
import './alpine-config';

// Custom functionality
document.addEventListener('DOMContentLoaded', () => {
  console.log('Skerritt Economics site initialized');
  
  // Initialize any custom components
  initializeCustomComponents();
});

function initializeCustomComponents() {
  // Smooth scroll for anchor links
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
  
  // Add loading states for forms
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;
      }
    });
  });
}