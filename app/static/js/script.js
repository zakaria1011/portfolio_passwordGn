$(document).ready(function(){
    $(#signupbutton).click(function(){
        var email = $("#email").val();
        var password = $("#email").val();
        var confirmPassword = $("#confirm-password").val();

        if(password !== confirmPassword){
            alert("Password do not match")
            return;
        }
        $.ajax({
            type: "POST",
            url: "/signup",
            contentType: "application/json",
            data: JSON.stringify({ email: email, password: password }),
            success: function(response) {
                window.location.href = "/signin"; 
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });

    });
});