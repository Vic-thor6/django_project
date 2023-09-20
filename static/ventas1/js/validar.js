document.addEventListener("DOMContentLoaded", function() {
    var formulario = document.getElementById("formulario-regstro");

    formulario.addEventListener("submit", function(event) {
        if (!validarFormulario()) {
            event.preventDefault();
        }
    });

    function validarFormulario() {
        var nombre = document.getElementById("nombre").value;
        var apellido = document.getElementById("apellido").value;
        var correo = document.getElementById("correo").value;
        var contrasena = document.getElementById("contrasena").value;
        var recontrasena = document.getElementById("recontrasena").value;
        var aceptaTerminos = document.getElementById("aceptaTerminos").checked;
        var mensajeError = "Obligatorio"

        if (nombre.trim() === "") {
            alert("El NOMBRE es un campo obligatorio");
            return false;
        } 
        
        if (apellido.trim() === "") {
            alert("El APELLIDO es un campo obligatorio");
            return false;
        }

        if (!correoValido(correo)) {
            alert("El CORREO es un campo obligatorio");
            return false;
        }

        if (contrasena !== recontrasena) {
            alert("Las contraseñas no coinciden");
        }
        if (validarContrasena(contrasena)) {
            alert("La contraseña no cumple con los requisitos de seguridad");
            return false;
        }
        if (!aceptaTerminos) {
            alert("Debes aceptar términos y condiciones");
            return false;
        }

        return true;
    }

    function correoValido(correo) {
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
    }

    function validarContrasena(contrasena) {
        if (contrasena.length < 8) {
            return false;
        }

        // Verificar si la contraseña contiene al menos un número
        var contieneNumero = /\d/.test(contrasena);

        // Verificar si la contraseña contiene al menos una letra minúscula
        var contieneLetraMinuscula = /[a-z]/.test(contrasena);

        // Verificar si la contraseña contiene al menos una letra mayúscula
        var contieneLetraMayuscula = /[A-Z]/.test(contrasena);

        // Verificar si la contraseña contiene al menos un carácter especial
        var contieneCaracterEspecial = /[@!#$%^&*()_+[\]{};':"\\|,.<>?~]/.test(contrasena);

        return contieneNumero && contieneLetraMinuscula && contieneLetraMayuscula && contieneCaracterEspecial;
    }
});
