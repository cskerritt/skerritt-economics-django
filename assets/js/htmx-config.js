/**
 * HTMX Configuration and Initialization
 */

import htmx from 'htmx.org';

// Make HTMX available globally
window.htmx = htmx;

// Configure HTMX
htmx.config.defaultSwapStyle = 'innerHTML';
htmx.config.defaultSwapDelay = 0;
htmx.config.defaultSettleDelay = 100;
htmx.config.includeIndicatorStyles = false;

// Add CSRF token to all HTMX requests
document.body.addEventListener('htmx:configRequest', (event) => {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
  if (csrfToken) {
    event.detail.headers['X-CSRFToken'] = csrfToken;
  }
});

// Handle HTMX errors
document.body.addEventListener('htmx:responseError', (event) => {
  console.error('HTMX request failed:', event.detail);
  // You can add user-friendly error handling here
});

// Loading indicators
document.body.addEventListener('htmx:beforeRequest', (event) => {
  const target = event.detail.target;
  target.classList.add('htmx-request');
});

document.body.addEventListener('htmx:afterRequest', (event) => {
  const target = event.detail.target;
  target.classList.remove('htmx-request');
});

console.log('HTMX initialized');