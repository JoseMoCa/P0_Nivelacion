from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UsuarioCrear(BaseModel):
    id: Optional[int] = None
    nombre_usuario: EmailStr
    contrasena: str = Field(None, min_length=8,max_length=16)
    imagen_perfil: Optional[str] = None

