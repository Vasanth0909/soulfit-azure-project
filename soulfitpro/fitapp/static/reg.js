function validate_form() {
    var name = document.getElementById('name').value;
    var address = document.getElementById('address').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var date = document.getElementById('date').value;
    var gender = document.querySelector('input[name="gender"]:checked');
    var age = document.getElementById('age').value;

    var error_message = document.getElementById('error_message');
    error_message.innerHTML = ''; // Clear previous error messages

    if (!name || !address || !email || !phone || !date || !gender || !age) {
        error_message.innerHTML = 'Please fill out all fields.';
        return false;
    }

    var email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email_regex.test(email)) {
        error_message.innerHTML = 'Invalid email format.';
        return false;
    }

    // Date format validation (dd/mm/yyyy)
    var date_regex = /^\d{2}\/\d{2}\/\d{4}$/;
    if (!date_regex.test(date)) {
        error_message.innerHTML = 'Invalid date format. Please use dd/mm/yyyy.';
        return false;
    }

    document.addEventListener('DOMContentLoaded', function () {
        const submitBtn = document.getElementById('submit-btn');
       
    
        submitBtn.addEventListener('click', function () {
            console.log('submit button clicked');
            const confirmation = confirm('Proceed to Register?');
            if (confirmation) {
            
                alert('Thank you for your register!');
                window.location.href = "home";
            }
        });

function showConfirmation() {
    var form = document.querySelector('.address_form');
    form.innerHTML = '<h2 align="center">Thanks for Registering!</h2>';
}
    return true;

})}