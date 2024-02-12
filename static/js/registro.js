document.addEventListener("DOMContentLoaded", function() {
    const formularioRegistro = document.getElementById('formulario-registro');

    formularioRegistro.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevenir el comportamiento de envío predeterminado

        const nombreUsuario = document.getElementById('nombre_usuario').value;
        const contrasena = document.getElementById('contrasena').value;

        // Crear el objeto de datos del usuario
        const datosUsuario = {
            nombre_usuario: nombreUsuario,
            contrasena: contrasena
        };

        // Enviar los datos al endpoint de creación de usuarios
        fetch( 'http://127.0.0.1:8000/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(datosUsuario),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Usuario creado con éxito:', data);
            // Aquí puedes redirigir al usuario o mostrar un mensaje de éxito
        })
        .catch((error) => {
            console.error('Error al crear el usuario:', error);
        });
    });
});
