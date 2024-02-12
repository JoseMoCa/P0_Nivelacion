document.addEventListener("DOMContentLoaded", function() {
    // Función para cargar tareas
    function cargarTareas() {
        fetch('http://127.0.0.1:8000/tareas')
            .then(response => response.json())
            .then(tareas => {
                const listaTareas = document.getElementById('tareas-lista');
                listaTareas.innerHTML = ''; // Limpiar lista actual
                tareas.forEach(tarea => {
                    const elemento = document.createElement('div');
                    elemento.textContent = tarea.texto; // Modifica según tu modelo
                    listaTareas.appendChild(elemento);
                });
            });
    }

    // Llama a cargarTareas al iniciar la app
    cargarTareas();
});
