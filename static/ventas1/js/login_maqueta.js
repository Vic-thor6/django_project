document.getElementById("login_ingreso").addEventListener("submit", function(event) {
    event.preventDefault();


    
        var email = document.getElementById("inputEmail").value;
        var password = document.getElementById("inputPassword").value;

        // simula que ingresa
        if (email === "123@123.cl" && password === "123") {
            alert("entro");
            window.location.href = '/ropa.html';
            
        } else {
            
            alert("Correo y/o contraseña incorrectos. Por favor, inténtalo de nuevo.");
            

        }

});