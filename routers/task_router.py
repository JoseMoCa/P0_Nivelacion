from fastapi import APIRouter, HTTPException
from typing import Dict, List
from datetime import datetime

from models.task_model import TareaCrear
from models.task_model import TareaActualizar
from models.user_model import UsuarioCrear
from models.category_model import CategoriaCrear

router = APIRouter()

fake_db_usuario: Dict[int, UsuarioCrear] = {}
fake_db_tareas: Dict[int, TareaCrear] = {}
fake_db_categorias: Dict[int, CategoriaCrear] = {}


@router.post("/tareas", response_model=TareaCrear)
async def crear_tarea(tarea: TareaCrear) -> TareaCrear:
    usuario_existentes = [
        usuario.nombre_usuario for usuario in fake_db_usuario.values()
    ]

    # Verifica si el id_usuario de la tarea existe en la lista de ids_usuario_existentes
    # if tarea.nombre_usuario not in usuario_existentes:
    #    raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Genera un ID único para la tarea
    tarea_id = len(fake_db_tareas) + 1

    # Fecha de creación de tarea
    tarea.fecha_creacion = datetime.now()

    # Crea y guarda la tarea en la base de datos simulada
    fake_db_tareas[tarea_id] = tarea.copy(update={"id": tarea_id})

    return fake_db_tareas[tarea_id]


@router.put("/tareas/{id_tarea}", response_model=TareaCrear)
async def actualizar_tarea(
    id_tarea: int, tarea_actualizacion: TareaActualizar
) -> TareaCrear:
    # Verificar si la tarea existe
    if id_tarea not in fake_db_tareas:
        raise HTTPException(status_code=404, detail="Tarea no existe")

    tarea_existente = fake_db_tareas[id_tarea]

    # Actualización de campos
    tarea_existente.texto = tarea_actualizacion.texto or tarea_existente.texto
    tarea_existente.fecha_finalizacion = (
        tarea_actualizacion.fecha_finalizacion or tarea_existente.fecha_finalizacion
    )
    tarea_existente.estado = tarea_actualizacion.estado or tarea_existente.estado

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
    tareas_usuario = [
        tarea for tarea in fake_db_tareas.values() if tarea.id_usuario == id_usuario
    ]

    if not tareas_usuario:
        raise HTTPException(
            status_code=404, detail="No se encontraron tareas para este usuario"
        )

    return tareas_usuario


@router.get("/tareas/{id_tarea}", response_model=TareaCrear)
async def obtener_tarea_por_id(id_tarea: int) -> TareaCrear:
    # Verificación de la tarea
    if id_tarea not in fake_db_tareas:
        raise HTTPException(status_code=404, detail="Tarea no existe")

    return fake_db_tareas[id_tarea]


@router.get("/debug/ver-base-tareas")
async def leer_tareas():
    return fake_db_tareas
