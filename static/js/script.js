// Simple client-side validation

document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            const requiredInputs = form.querySelectorAll("input[required]");

            for (let input of requiredInputs) {
                if (!input.value.trim()) {
                    alert("Please fill all required fields");
                    e.preventDefault();
                    return;
                }
            }
        });
    });

});
