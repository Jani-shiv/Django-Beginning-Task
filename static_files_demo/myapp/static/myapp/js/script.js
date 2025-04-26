// Change navbar color on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Simple alert on page load
window.addEventListener('DOMContentLoaded', () => {
    console.log("Page fully loaded. Welcome to the Static Files Demo!");
});
