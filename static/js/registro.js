document.addEventListener("DOMContentLoaded",
    function () {
        const formularioRegistro = document.getElementById('register-form');

        formularioRegistro.addEventListener('submit', function (event) {
            event.preventDefault();  // Prevenir el comportamiento de envío predeterminado

            const nombreUsuario = document.getElementById('nombre_usuario').value;
            const contrasena = document.getElementById('contrasena').value;
            let profilePicUrl = this.querySelector('input[type="url"]').value;
            // Establecer una URL por defecto para la foto de perfil si el campo está vacío
            if (!profilePicUrl) {
                profilePicUrl = 'https://media.istockphoto.com/id/172177007/es/foto/luchador-de-negocios.jpg?s=1024x1024&w=is&k=20&c=p5IhWikTVVgBjIkelZ-mpOnNtcZZbW07y3-Fr66WQGs=';
            }
            // Crear el objeto de datos del usuario
            const datosUsuario = {
                nombre_usuario: nombreUsuario,
                contrasena: contrasena,
                imagen_perfil: profilePicUrl
            };

            // Enviar los datos al endpoint de creación de usuarios
            fetch('http://127.0.0.1:8000/usuarios', {
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
