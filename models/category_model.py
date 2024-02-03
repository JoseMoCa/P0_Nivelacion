from pydantic import BaseModel, Field
from typing import Optional

class CategoriaCrear(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(..., max_length=12)
    descripcion: str = Field(..., max_length=80)
