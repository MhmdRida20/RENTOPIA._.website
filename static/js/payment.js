function showAlert() {
    var nameCard = document.getElementById("name_card").value;
    var cardNumber = document.getElementById("cardNumber").value;
    var expiration = document.getElementById("expiration").value;
    var cvv = document.getElementById("cvv").value;
    var check = document.getElementById("check");

    // Validate form inputs
    if (nameCard === "" || cardNumber === "" || expiration === "" || cvv === "" || !check.checked) {
        var alertDiv = document.createElement("div");
        alertDiv.className = "alert";
        alertDiv.textContent = "All fields should be filled, and the checkbox should be checked.";
        document.body.appendChild(alertDiv);
        setTimeout(function() {
            alertDiv.remove();
        }, 5000);
        return;
    }
    var paymentForm = document.getElementById("payment-form");
    var submitButton = document.getElementById("submit");

    var isConfirmed = confirm("Are you sure you want to proceed with the payment?");

    if (isConfirmed) {
        submitButton.disabled = true;
        var formData = new FormData(paymentForm);
        var landId = submitButton.getAttribute("data-land-id");
        var url = "/api/payment/" + landId;
        fetch(url, {
            method: "POST", 
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Handle the success response
                alert("Payment completed successfully!");
                window.location.href = "http://127.0.0.1:5000/home";
            
            } else {
                // Handle the error response
                alert("Payment processing failed. Error: " + data.error);
            }
        })
        .catch(error => {
            // Handle any network or server errors
            alert("Payment processing failed. Error: " + error.message);
        })
        .finally(() => {
            // Re-enable the submit button
            submitButton.disabled = false;
            
        });
    }
    
}

document.getElementById("submit").addEventListener("click", showAlert);