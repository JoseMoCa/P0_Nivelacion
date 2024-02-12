document.addEventListener('DOMContentLoaded',
    (event) => {

// Función para registrar un nuevo usuario
        function registrarUsuario(nombreusuario, contrasena) {
            fetch('http://127.0.0.1:8000/usuarios', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nombre_usuario: nombreusuario,
                    contrasena: contrasena
                })
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al registrar el usuario');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Registro exitoso:', data);
                    alert('Registro exitoso. Por favor, inicia sesión.');
                    // Opcional: cambiar automáticamente al formulario de inicio de sesión después del registro
                    document.getElementById('register-form').style.display = 'none';
                    document.getElementById('login-form').style.display = 'block';
                })
                .then(data => {
                    console.log('Registro/Inicio de sesión exitoso:', data);
                    // Almacenar el token en localStorage
                    localStorage.setItem('token', data.access_token);
                    // Redirigir al usuario a user-home.html
                    window.location.href = 'http://127.0.0.1:8000/user-home.html';  // Asegúrate de que la ruta sea correcta
                })
                .catch((error) => {
                    console.error('Error en el registro:', error);
                });
        }


// Función para iniciar sesión
        function iniciarSesion(nombreusuario, contrasena) {
            fetch('http://127.0.0.1:8000/usuarios/iniciar-sesion', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nombre_usuario: nombreusuario,
                    contrasena: contrasena
                })
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Credenciales inválidas');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Inicio de sesión exitoso:', data);
                    // Almacenar el token en localStorage y redirigir al usuario
                    localStorage.setItem('token', data.access_token);
                    window.location.href = 'http://127.0.0.1:8000/user-home.html';
                })
                .catch((error) => {
                    console.error('Error en el inicio de sesión:', error);
                });
        }

// Eventos para los formularios
        document.getElementById('register-form').addEventListener('submit', function (event) {
            event.preventDefault();
            const nombreusuario = this.querySelector('input[type="text"]').value;
            const contrasena = this.querySelector('input[type="password"]').value;
            registrarUsuario(nombreusuario, contrasena);
        });

        document.getElementById('login-form').addEventListener('submit', function (event) {
            event.preventDefault();
            const nombreusuario = this.querySelector('input[type="text"]').value;
            const contrasena = this.querySelector('input[type="password"]').value;
            iniciarSesion(nombreusuario, contrasena);
        });
    });
