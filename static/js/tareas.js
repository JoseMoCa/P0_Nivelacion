document.addEventListener('DOMContentLoaded', (event) => {
    cargarTareas();  // Función para cargar tareas al cargar la página

    document.getElementById('new-task-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const nombreTarea = this.querySelector('input[type="text"]').value;
        const descripcion = this.querySelector('textarea').value;
        crearNuevaTarea(nombreTarea, descripcion);  // Función para crear una nueva tarea
    });
});

function cargarTareas() {
    // Aquí iría la lógica para cargar las tareas del backend y mostrarlas en #tasks-list
}

function crearNuevaTarea(nombreTarea, descripcion) {
    // Aquí iría la lógica para enviar la nueva tarea al backend y actualizar la lista de tareas
}