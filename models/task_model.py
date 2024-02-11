from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TareaCrear(BaseModel):
    id: Optional[int] = None
    texto: str = Field(..., min_length=4, max_length=120)
    fecha_creacion: Optional[datetime] = None
    fecha_finalizacion: Optional[datetime] = None
    estado: str  # lista de estados, por definir
    id_categoria: int
    id_usuario: int


class TareaActualizar(BaseModel):
    texto: Optional[str] = None
    fecha_finalizacion: Optional[datetime] = None
    estado: Optional[str] = None


