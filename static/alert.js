document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert.fade-out');
        alerts.forEach(function(alert) {
            alert.classList.add('fade');
            setTimeout(function() {
                alert.style.display = 'none';
            }, 300); // Match this duration with the CSS transition duration
        });
    }, 3000); // Time in milliseconds before the alert starts to fade out
});