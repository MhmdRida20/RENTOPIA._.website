function validateDate() {
    var dateOfBirth = document.getElementById("dateOfBirth").value;
    if (!dateOfBirth) {
        var alertDiv = document.createElement("div");
        alertDiv.className = "alert";
        alertDiv.textContent = "Date Should be Selected!";
        document.body.appendChild(alertDiv);
        setTimeout(function () {
            alertDiv.remove();
        }, 5000);
    } else {
        window.location.href = "home.html";
    }
}
document.getElementById("next").addEventListener("click",validateDate);