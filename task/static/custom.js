document.addEventListener("DOMContentLoaded", function() {
    // Simple hover effect enhancement
    document.querySelectorAll('.task-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-3px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
});