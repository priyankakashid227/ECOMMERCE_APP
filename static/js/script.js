// Simple JS for future enhancements

// Example: Flash message auto-hide
window.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = "none";
        }, 3000); // Hide after 3 seconds
    });
});
