


(function () {
    'use strict'
    var forms = document.querySelectorAll('.needs-validation')
    Array.from(forms).map(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})()