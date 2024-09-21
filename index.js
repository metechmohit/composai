// Add animations or other interactive behaviors here
document.addEventListener('DOMContentLoaded', function() {
    const ctaBtn = document.querySelector('.cta-btn');
    ctaBtn.addEventListener('mouseover', function() {
        ctaBtn.style.backgroundColor = '#2c6bc1';
    });

    ctaBtn.addEventListener('mouseout', function() {
        ctaBtn.style.backgroundColor = '#4a90e2';
    });
});
