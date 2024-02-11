from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UsuarioCrear(BaseModel):
    id_usuario: Optional[int] = None
    nombre_usuario: str
    contrasena: str = Field(None, min_length=8, max_length=16)
    imagen_perfil: Optional[str] = None
    usuario_cifrado: Optional[str] = None


class CredencialesUsuario(BaseModel):
    nombre_usuario: str
    contrasena: str
