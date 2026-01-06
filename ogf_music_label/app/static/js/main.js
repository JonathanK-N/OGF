// Main JavaScript file for OGF Music Label

// Initialize GSAP
gsap.registerPlugin(ScrollTrigger);

// Global variables
let isLoading = false;
let currentTheme = 'dark';

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Initialize application
function initializeApp() {
    setupGlobalAnimations();
    setupNavigation();
    setupScrollEffects();
    setupMusicPlayer();
    setupContactForm();
    setupImageLazyLoading();
    setupPerformanceOptimizations();
}

// Global animations setup
function setupGlobalAnimations() {
    // Page load animation
    gsap.from("body", {
        opacity: 0,
        duration: 0.5,
        ease: "power2.out"
    });
    
    // Smooth scroll to anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                gsap.to(window, {
                    duration: 1,
                    scrollTo: target,
                    ease: "power2.inOut"
                });
            }
        });
    });
}

// Navigation setup
function setupNavigation() {
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    // Navbar scroll effect
    let lastScrollTop = 0;
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            gsap.to(navbar, {
                y: -100,
                duration: 0.3,
                ease: "power2.out"
            });
        } else {
            // Scrolling up
            gsap.to(navbar, {
                y: 0,
                duration: 0.3,
                ease: "power2.out"
            });
        }
        
        lastScrollTop = scrollTop;
        
        // Change navbar background on scroll
        if (scrollTop > 50) {
            navbar.classList.add('bg-ogf-dark/95');
            navbar.classList.remove('bg-ogf-dark/90');
        } else {
            navbar.classList.add('bg-ogf-dark/90');
            navbar.classList.remove('bg-ogf-dark/95');
        }
    });
    
    // Mobile menu toggle
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            const isOpen = !mobileMenu.classList.contains('hidden');
            
            if (isOpen) {
                gsap.to(mobileMenu, {
                    height: 0,
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.out",
                    onComplete: () => {
                        mobileMenu.classList.add('hidden');
                    }
                });
            } else {
                mobileMenu.classList.remove('hidden');
                gsap.fromTo(mobileMenu, 
                    { height: 0, opacity: 0 },
                    { height: 'auto', opacity: 1, duration: 0.3, ease: "power2.out" }
                );
            }
        });
    }
}

// Scroll effects setup
function setupScrollEffects() {
    // Parallax effect for hero sections
    gsap.utils.toArray('.hero-gradient').forEach(hero => {
        gsap.to(hero, {
            yPercent: -50,
            ease: "none",
            scrollTrigger: {
                trigger: hero,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    });
    
    // Fade in animations for sections
    gsap.utils.toArray('section').forEach(section => {
        gsap.from(section.children, {
            y: 50,
            opacity: 0,
            duration: 1,
            stagger: 0.2,
            ease: "power2.out",
            scrollTrigger: {
                trigger: section,
                start: "top 80%",
                toggleActions: "play none none reverse"
            }
        });
    });
    
    // Progress bar
    gsap.to(".progress-bar", {
        scaleX: 1,
        ease: "none",
        scrollTrigger: {
            trigger: "body",
            start: "top top",
            end: "bottom bottom",
            scrub: true
        }
    });
}

// Music player setup
function setupMusicPlayer() {
    const playButtons = document.querySelectorAll('.play-btn, .quick-action');
    
    playButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Animate button
            gsap.to(this, {
                scale: 0.9,
                duration: 0.1,
                yoyo: true,
                repeat: 1,
                ease: "power2.out"
            });
            
            // Simulate music playing
            const icon = this.querySelector('i');
            if (icon) {
                if (icon.classList.contains('fa-play')) {
                    icon.classList.remove('fa-play');
                    icon.classList.add('fa-pause');
                    this.classList.add('playing');
                } else {
                    icon.classList.remove('fa-pause');
                    icon.classList.add('fa-play');
                    this.classList.remove('playing');
                }
            }
        });
    });
}

// Contact form setup
function setupContactForm() {
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (isLoading) return;
            
            isLoading = true;
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<div class="loading"></div> Envoi en cours...';
            submitBtn.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {
                // Success state
                submitBtn.innerHTML = '<i class="fas fa-check mr-2"></i>Message envoyé !';
                submitBtn.classList.add('bg-green-500');
                submitBtn.classList.remove('from-ogf-purple', 'to-ogf-gold');
                
                // Reset form
                this.reset();
                
                // Reset button after 3 seconds
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.classList.remove('bg-green-500');
                    submitBtn.classList.add('from-ogf-purple', 'to-ogf-gold');
                    submitBtn.disabled = false;
                    isLoading = false;
                }, 3000);
            }, 2000);
        });
        
        // Form validation
        const inputs = contactForm.querySelectorAll('input[required], textarea[required], select[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', validateField);
            input.addEventListener('input', clearValidation);
        });
    }
}

// Field validation
function validateField(e) {
    const field = e.target;
    const value = field.value.trim();
    
    // Remove existing validation
    clearValidation(e);
    
    if (!value) {
        showFieldError(field, 'Ce champ est requis');
        return false;
    }
    
    // Email validation
    if (field.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Veuillez entrer une adresse email valide');
            return false;
        }
    }
    
    // Show success
    showFieldSuccess(field);
    return true;
}

// Clear field validation
function clearValidation(e) {
    const field = e.target;
    field.classList.remove('border-red-500', 'border-green-500');
    
    const errorMsg = field.parentNode.querySelector('.error-message');
    if (errorMsg) {
        errorMsg.remove();
    }
}

// Show field error
function showFieldError(field, message) {
    field.classList.add('border-red-500');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message text-red-400 text-sm mt-1';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
    
    // Animate error message
    gsap.from(errorDiv, {
        opacity: 0,
        y: -10,
        duration: 0.3,
        ease: "power2.out"
    });
}

// Show field success
function showFieldSuccess(field) {
    field.classList.add('border-green-500');
}

// Image lazy loading
function setupImageLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Performance optimizations
function setupPerformanceOptimizations() {
    // Debounce scroll events
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(() => {
            // Scroll-dependent operations
        }, 10);
    });
    
    // Preload critical resources
    const criticalImages = [
        '/static/images/logo.png',
        '/static/images/hero-bg.jpg'
    ];
    
    criticalImages.forEach(src => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = src;
        document.head.appendChild(link);
    });
}

// Utility functions
const utils = {
    // Throttle function
    throttle: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Debounce function
    debounce: function(func, wait, immediate) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                timeout = null;
                if (!immediate) func(...args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func(...args);
        };
    },
    
    // Format number with commas
    formatNumber: function(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    
    // Generate random ID
    generateId: function() {
        return Math.random().toString(36).substr(2, 9);
    },
    
    // Check if element is in viewport
    isInViewport: function(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
};

// Export utils for global use
window.OGFUtils = utils;

// Console welcome message
console.log(`
🎵 OGF - Only God & Family 🎵
Website loaded successfully!
Built with Flask, Tailwind CSS & GSAP
`);

// Service Worker registration (for PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}