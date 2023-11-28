
document.addEventListener('DOMContentLoaded', function () {
    const registerBtn = document.getElementById('register-btn');
    const closeBtn = document.getElementById('close-btn');

    registerBtn.addEventListener('click', function () {
        console.log('Register button clicked');
        const confirmation = confirm('Proceed to Register?');
        if (confirmation) {
            window.location.href = "register";
        }
    });

    closeBtn.addEventListener('click', function () {
        console.log('Close button clicked');
        window.history.back();
    });
});
