from fastapi import APIRouter, HTTPException
from typing import Dict, List
from datetime import datetime

from models.task_model import TareaCrear
from models.task_model import TareaActualizar
from models.user_model import UsuarioCrear
from models.category_model import CategoriaCrear

router = APIRouter()


fake_db_tareas: Dict[int, TareaCrear] = {}
fake_db_usuarios: Dict[int, UsuarioCrear] = {}
fake_db_categorias: Dict[int, CategoriaCrear] = {}


@router.post("/tareas", response_model=TareaCrear)
async def crear_tarea(tarea: TareaCrear) -> TareaCrear:
    # Verificar si el usuario existe
    if tarea.id_usuario not in fake_db_usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar si la categoría existe
    if tarea.id_categoria not in fake_db_categorias:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    # Genera un ID único para la tarea
    tarea_id = len(fake_db_tareas) + 1
    # Fecha de creación de tarea
    tarea.fecha_creacion = datetime.now()

    # Aquí podrías agregar lógica para verificar si el usuario y la categoría existen

    fake_db_tareas[tarea_id] = tarea.copy(update={"id": tarea_id})

    return fake_db_tareas[tarea_id]


@router.put("/tareas/{id_tarea}", response_model=TareaCrear)
async def actualizar_tarea(id_tarea: int, tarea_actualizacion: TareaActualizar) -> TareaCrear:
    # Verificar si la tarea existe
    if id_tarea not in fake_db_tareas:
        raise HTTPException(status_code=404, detail="Tarea no existe")
    # Actualización
    if tarea_actualizacion.texto is not None:
        tarea_existente.texto = tarea_actualizacion.texto
    if tarea_actualizacion.fecha_finalizacion is not None:
        tarea_existente.fecha_finalizacion = tarea_actualizacion.fecha_finalizacion
    if tarea_actualizacion.estado is not None:
        tarea_existente.estado = tarea_actualizacion.estado

    tarea_existente = fake_db_tareas[id_tarea]

    # Actualizar los campos de la tarea
    update_data = tarea_actualizacion.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(tarea_existente, key, value)

    fake_db_tareas[id_tarea] = tarea_existente
    return tarea_existente


@router.delete("/tareas/{id_tarea}", status_code=200)
async def eliminar_tarea(id_tarea: int):
    # Verificación de la tarea
    if id_tarea not in fake_db_tareas:
        raise HTTPException(status_code=404, detail="Tarea no existe")

    # Eliminación
    del fake_db_tareas[id_tarea]

    return {"mensaje": "Tarea eliminada"}


@router.get("/tareas/usuario/{id_usuario}", response_model=List[TareaCrear])
async def obtener_tareas_por_usuario(id_usuario: int) -> List[TareaCrear]:
    # Filtra las tareas de un usuario
    tareas_usuario = [tarea for tarea in fake_db_tareas.values() if tarea.id_usuario == id_usuario]

    if not tareas_usuario:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")

    return tareas_usuario


@router.get("/tareas/{id_tarea}", response_model=TareaCrear)
async def obtener_tarea_por_id(id_tarea: int) -> TareaCrear:
    # Verificación de la tarea
    if id_tarea not in fake_db_tareas:
        raise HTTPException(status_code=404, detail="Tarea no existe")

    return fake_db_tareas[id_tarea]


