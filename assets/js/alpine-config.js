/**
 * Alpine.js Configuration and Initialization
 */

import Alpine from 'alpinejs';

// Make Alpine available globally
window.Alpine = Alpine;

// Register Alpine stores
Alpine.store('navigation', {
  mobileMenuOpen: false,
  toggleMobileMenu() {
    this.mobileMenuOpen = !this.mobileMenuOpen;
  }
});

// Register Alpine data components
Alpine.data('dropdown', () => ({
  open: false,
  toggle() {
    this.open = !this.open;
  },
  close() {
    this.open = false;
  }
}));

Alpine.data('modal', () => ({
  show: false,
  open() {
    this.show = true;
  },
  close() {
    this.show = false;
  }
}));

// Start Alpine
Alpine.start();

console.log('Alpine.js initialized');