from fastapi import APIRouter, HTTPException
from typing import Dict, List
from models.category_model import CategoriaCrear

router = APIRouter()

fake_db_categorias: Dict[int, CategoriaCrear] = {}

@router.post("/categorias", response_model=CategoriaCrear)
async def crear_categoria(categoria: CategoriaCrear) -> CategoriaCrear:
    # Generar un ID único
    categoria_id = len(fake_db_categorias) + 1
    for cat in fake_db_categorias.values():
        if cat.nombre == categoria.nombre:
            raise HTTPException(status_code=400, detail="La categoría ya existe")

    categoria_creada = categoria.copy(update={"id_categ": categoria_id})
    fake_db_categorias[categoria_id] = categoria_creada

    return categoria_creada

@router.delete("/categorias/{id_categ}", status_code=200)
async def eliminar_categoria(id_categ: int):
    if id_categ not in fake_db_categorias:
        raise HTTPException(status_code=404, detail="La categoría no existe")

    del fake_db_categorias[id_categ]

    return {"mensaje": "Categoría eliminada correctamente"}


@router.get("/categorias", response_model=List[CategoriaCrear])
async def obtener_categorias():
    return list(fake_db_categorias.values())


@router.get("/debug/ver-base-categ")
async def leer_categ():
    return fake_db_categorias


