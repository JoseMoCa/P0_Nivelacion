from pydantic import BaseModel, Field
from typing import Optional

class CategoriaCrear(BaseModel):
    id_categ: Optional[int] = None
    nombre: str = Field(..., max_length=20)
    descripcion: str = Field(..., max_length=100)

