import bcrypt
import jwt
from fastapi import APIRouter, HTTPException, status
from models.user_model import UsuarioCrear
from typing import Dict
from datetime import datetime, timedelta
from pydantic import BaseModel

SECRET_KEY = "mipez"
ALGORITHM = "HS256"

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

# Un ejemplo de base de datos simulada como un diccionario
fake_db_usuario: Dict[str, UsuarioCrear] = {}

@router.post("/usuarios", response_model=UsuarioCrear)
async def crear_usuario(usuario: UsuarioCrear) -> UsuarioCrear:
    # Lógica para generar un ID único
    usuario.id = len(fake_db_usuario) + 1
    if usuario.nombre_usuario in [u.nombre_usuario for u in fake_db_usuario.values()]:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Cifrado de la contraseña
    hashed_password = bcrypt.hashpw(usuario.contrasena.encode('utf-8'), bcrypt.gensalt())
    usuario_cifrado = usuario.copy(update={"contrasena": hashed_password.decode('utf-8')})

    # Simulación del almacenamiento en base de datos
    fake_db_usuario[usuario.id] = usuario_cifrado

    # Devuelve los datos del usuario (sin incluir la contraseña real)
    usuario_creado = usuario_cifrado.dict()
    del usuario_creado["contrasena"]
    return usuario_creado


@router.post("/usuarios/iniciar-sesion", response_model=Token)
async def iniciar_sesion(nombre_usuario: str, contrasena: str):
    usuario = fake_db_usuario.get(nombre_usuario)

    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    if not bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    # Crear un token JWT
    data_token = {
        "sub": usuario.nombre_usuario,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(data_token, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}