function validateform() {
    var email = document.getElementById("email").value;
    var fullname = document.getElementById("fullname").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var phone = document.getElementById("phone").value;
    if (email=="" || fullname=="" || username=="" || password=="" || phone=="") {
        var alertDiv = document.createElement("div");
        alertDiv.className = "alert";
        alertDiv.textContent = "All Fields should be filled";
        document.body.appendChild(alertDiv);
        setTimeout(function () {
            alertDiv.remove();
        }, 5000);
    }else{
        window.location.href = "birth_profile.html";
    }
}

document.getElementById("signup_but").addEventListener("click", validateform)
