document.addEventListener('DOMContentLoaded', function() {
    // Function to check if an element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.left <= (window.innerWidth || document.documentElement.clientWidth) &&
            rect.bottom >= 0 &&
            rect.right >= 0
        );
    }
    
    // Add transition delay to all animated elements based on their position
    function setAnimationDelays() {
        // Process each animation container separately
        document.querySelectorAll('.animation-container').forEach(container => {
            const elements = container.querySelectorAll('.animate-element');
            elements.forEach((element, index) => {
                // Set a delay based on element index (100ms increments)
                element.style.transitionDelay = (index * 0.1) + 's';
            });
        });
        
        // For elements not in an animation container, handle in groups by parent
        const nonContainerElements = document.querySelectorAll('.animate-element:not(.animation-container .animate-element)');
        let currentParent = null;
        let parentIndex = 0;
        let childIndex = 0;
        
        nonContainerElements.forEach((element) => {
            if (element.parentElement !== currentParent) {
                currentParent = element.parentElement;
                parentIndex++;
                childIndex = 0;
            }
            
            // Set delay based on parent group and child position
            element.style.transitionDelay = (0.1 * childIndex) + 's';
            childIndex++;
        });
    }
    
    // Function to handle the animation of visible elements
    function handleScrollAnimation() {
        const elements = document.querySelectorAll('.animate-element');
        
        elements.forEach(function(element) {
            if (isInViewport(element)) {
                element.classList.add('visible');
            }
        });
    }
    
    // Set animation delays
    setAnimationDelays();
    
    // Initial check on page load (with a small delay to ensure elements are fully rendered)
    setTimeout(handleScrollAnimation, 100);
    
    // Check on scroll
    window.addEventListener('scroll', handleScrollAnimation);
    
    // Also check on resize
    window.addEventListener('resize', handleScrollAnimation);
    
    // Debug - check if the button has animation applied
    console.log('Button element:', document.querySelector('.btn.animate-element'));
});