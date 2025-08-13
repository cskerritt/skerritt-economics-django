// Enhanced JavaScript with Mobile Menu, Dark Mode, and Animations

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initMobileMenu();
    initStickyNav();
    initDarkMode();
    initScrollProgress();
    initBackToTop();
    initLazyLoading();
    initKeyboardNavigation();
    initActivePageHighlighting();
    initSearchFunctionality();
    initAnimations();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.navbar-menu');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            menuToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Accessibility
            const isExpanded = menuToggle.classList.contains('active');
            menuToggle.setAttribute('aria-expanded', isExpanded);
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
        
        // Handle dropdown toggles on mobile
        const dropdowns = document.querySelectorAll('.has-dropdown > a');
        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    this.parentElement.classList.toggle('active');
                }
            });
        });
    }
}

// Sticky Navigation
function initStickyNav() {
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.classList.add('sticky');
            
            // Hide on scroll down, show on scroll up
            if (currentScroll > lastScroll) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }
        } else {
            navbar.classList.remove('sticky');
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
}

// Dark Mode Toggle
function initDarkMode() {
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    // Create dark mode toggle button
    const themeToggle = document.createElement('button');
    themeToggle.className = 'theme-toggle';
    themeToggle.innerHTML = currentTheme === 'dark' ? '☀️' : '🌙';
    themeToggle.setAttribute('aria-label', 'Toggle dark mode');
    document.body.appendChild(themeToggle);
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        themeToggle.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
    });
}

// Scroll Progress Bar
function initScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    });
}

// Back to Top Button
function initBackToTop() {
    const backToTop = document.createElement('button');
    backToTop.className = 'back-to-top';
    backToTop.innerHTML = '↑';
    backToTop.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTop);
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Lazy Loading for Images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                    img.classList.add('fade-in');
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for older browsers
        images.forEach(img => {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    }
}

// Keyboard Navigation for Dropdowns
function initKeyboardNavigation() {
    const dropdowns = document.querySelectorAll('.has-dropdown');
    
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('a');
        const menu = dropdown.querySelector('.dropdown-menu');
        
        if (link && menu) {
            // Make dropdown accessible
            link.setAttribute('aria-haspopup', 'true');
            link.setAttribute('aria-expanded', 'false');
            
            // Keyboard events
            link.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    const isExpanded = this.getAttribute('aria-expanded') === 'true';
                    this.setAttribute('aria-expanded', !isExpanded);
                    menu.style.display = isExpanded ? 'none' : 'block';
                }
            });
            
            // Tab navigation
            const menuItems = menu.querySelectorAll('a');
            const lastItem = menuItems[menuItems.length - 1];
            
            lastItem.addEventListener('keydown', function(e) {
                if (e.key === 'Tab' && !e.shiftKey) {
                    link.setAttribute('aria-expanded', 'false');
                    menu.style.display = 'none';
                }
            });
        }
    });
    
    // Escape key to close menus
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const openMenus = document.querySelectorAll('[aria-expanded="true"]');
            openMenus.forEach(menu => {
                menu.setAttribute('aria-expanded', 'false');
                const dropdown = menu.nextElementSibling;
                if (dropdown) dropdown.style.display = 'none';
            });
        }
    });
}

// Active Page Highlighting
function initActivePageHighlighting() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-menu a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
            
            // If in dropdown, highlight parent too
            const parentDropdown = link.closest('.has-dropdown');
            if (parentDropdown) {
                parentDropdown.querySelector('a').classList.add('active-parent');
            }
        }
    });
}

// Search Functionality
function initSearchFunctionality() {
    // Create search overlay
    const searchOverlay = document.createElement('div');
    searchOverlay.className = 'search-overlay';
    searchOverlay.innerHTML = `
        <div class="search-container">
            <input type="text" class="search-input" placeholder="Search services, locations, or resources...">
            <button class="search-close">×</button>
            <div class="search-results"></div>
        </div>
    `;
    document.body.appendChild(searchOverlay);
    
    // Add search button to navigation
    const searchBtn = document.createElement('button');
    searchBtn.className = 'search-btn';
    searchBtn.innerHTML = '🔍';
    searchBtn.setAttribute('aria-label', 'Search');
    
    const navbar = document.querySelector('.navbar-menu');
    if (navbar) {
        const li = document.createElement('li');
        li.appendChild(searchBtn);
        navbar.appendChild(li);
    }
    
    // Search functionality
    const searchInput = searchOverlay.querySelector('.search-input');
    const searchClose = searchOverlay.querySelector('.search-close');
    const searchResults = searchOverlay.querySelector('.search-results');
    
    searchBtn.addEventListener('click', function() {
        searchOverlay.classList.add('active');
        searchInput.focus();
    });
    
    searchClose.addEventListener('click', function() {
        searchOverlay.classList.remove('active');
        searchInput.value = '';
        searchResults.innerHTML = '';
    });
    
    // Keyboard shortcut (Ctrl/Cmd + K)
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            searchOverlay.classList.add('active');
            searchInput.focus();
        }
    });
    
    // Simple search implementation
    searchInput.addEventListener('input', debounce(function() {
        const query = this.value.toLowerCase();
        if (query.length < 2) {
            searchResults.innerHTML = '';
            return;
        }
        
        // Mock search results - replace with actual search API
        const mockResults = [
            { title: 'Forensic Economics', url: '/services/forensic-economics/' },
            { title: 'Business Valuation', url: '/services/business-valuation/' },
            { title: 'Life Care Planning', url: '/services/life-care-planning/' },
            { title: 'Rhode Island Services', url: '/locations/rhode-island/' },
            { title: 'Massachusetts Services', url: '/locations/massachusetts/' }
        ].filter(item => item.title.toLowerCase().includes(query));
        
        if (mockResults.length > 0) {
            searchResults.innerHTML = mockResults.map(result => `
                <a href="${result.url}" class="search-result-item">
                    <span>${result.title}</span>
                    <span class="search-result-arrow">→</span>
                </a>
            `).join('');
        } else {
            searchResults.innerHTML = '<div class="no-results">No results found</div>';
        }
    }, 300));
}

// Scroll Animations
function initAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if ('IntersectionObserver' in window) {
        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, { threshold: 0.1 });
        
        animatedElements.forEach(el => animationObserver.observe(el));
    }
}

// Utility: Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func.apply(this, args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// WebP Support Detection
function supportsWebP() {
    const canvas = document.createElement('canvas');
    canvas.width = 1;
    canvas.height = 1;
    return canvas.toDataURL('image/webp').indexOf('image/webp') === 0;
}

// Convert images to WebP with fallback
function initWebPSupport() {
    if (supportsWebP()) {
        document.documentElement.classList.add('webp');
    } else {
        document.documentElement.classList.add('no-webp');
    }
}

// Initialize WebP support
initWebPSupport();