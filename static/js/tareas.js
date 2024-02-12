document.addEventListener('DOMContentLoaded', (event) => {
    // Configurar event listeners para formularios y botones
    configurarFormulariosYBotones();
});

function configurarFormulariosYBotones() {
    // Configuración de eventos para crear, actualizar y eliminar tareas
    document.getElementById('new-task-form').addEventListener('submit', CreacionTarea);

    // Añade aquí la configuración para los botones o formularios de actualizar y eliminar tareas
}

function CreacionTarea(event) {
    event.preventDefault();
    const textoTarea = document.querySelector('#new-task-form input[type="text"]').value;
    const idUsuario = localStorage.getItem('idUsuario');  // Asume que esta el ID del usuario en localStorage
    const estadoInicial = "pendiente";  // Asumiendo un estado inicial para nuevas tareas
    const idCategoria = document.querySelector('#new-task-form select[name="categoria"]').value;  //
    const fechaFinalizacion = document.querySelector('#new-task-form input[type="date"]').value; // Asume que hay un input de tipo 'date' para la fecha de finalización

    // La fecha de creación se establece en el cliente; la fecha de finalización inicialmente es null
    const fechaCreacion = new Date().toISOString();

    fetch('/crear_tarea', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Incluir el token de autenticación si es necesario
        },
        body: JSON.stringify({
            id_usuario: idUsuario,
            texto: textoTarea,
            fecha_creacion: fechaCreacion,
            fecha_finalizacion: fechaFinalizacion,
            estado: estadoInicial,
            id_categoria: idCategoria
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al crear tarea');
        }
        return response.json();
    })
    .then(data => {
        console.log('Tarea creada:', data);
        const listaTareas = document.getElementById('tasks-list');
        const tareaElemento = document.createElement('div');
        tareaElemento.textContent = `${data.texto} - Fecha de Finalización: ${data.fecha_finalizacion}`;
        listaTareas.appendChild(tareaElemento);
    })
    .catch(error => console.error('Error:', error));
}



// Añade funciones similares para manejar la actualización y elimina
