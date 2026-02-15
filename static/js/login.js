function validateForm(){
    var useremail=document.getElementById("useremail").value;
    var password=document.getElementById("password").value;
    if (useremail=="" || password=="") {
        var alertDiv = document.createElement("div");
        alertDiv.className = "alert";
        alertDiv.textContent = "All Fields should be filled";
        document.body.appendChild(alertDiv);
        setTimeout(function () {
            alertDiv.remove();
        }, 5000);
    }else{[]
        window.location.href = "home.html";
    }
}
document.getElementById("login_but").addEventListener("click", validateForm)
