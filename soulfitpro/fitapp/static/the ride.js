document.addEventListener('DOMContentLoaded', function () {
    const registerBtn = document.getElementById('register-btn');
    const closeBtn = document.getElementById('close-btn');

    registerBtn.addEventListener('click', function () {
        const confirmation = confirm('Proceed to Register?');
        if (confirmation) {
            window.location.href = "register";
        }
    });
    closeBtn.addEventListener('click', function () {
        window.history.back();


      });})

