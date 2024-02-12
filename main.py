# Desarrollo de Aplicación WEB - NIVELATORIO PROYECTO 0

#  PASO 0
# Creación de Entorno:  este paso es clave para "ayudar a mantener las dependencias requeridas
# por diferentes proyectos separadas al crear un entorno aislado para cada proyecto"
#    python -m venv entorno_web_1

# Activación del entorno:
#    source entorno_web_1/bin/activate

# Instalación de FastAPI y de Uvicorn: clave usar este framework para construir APIs en Pyhton,
# es agil y de alta escalabilidad; mientras que Uvicorn es un servidor asincronico.
#    pip install fastapi uvicorn bcrypt pytest pydantic sqlalchemy pymysql pyjwt pydantic[email]
# si quiero actualizar PIP:
#    pip install --upgrade pip
#    pip install pydantic[email]

### PASO 1  (lo que escribí en archivo)

### PASO 2 (Correr el appweb, pero debo inicializar el servidor Uvicorn)
#   uvicorn main:app --reload

# PASO 3 (Test)  correr test:   pytest

## DESARROLLO: ##
import bcrypt
import jwt

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user_router, category_router, task_router

app = FastAPI()

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir los routers en la aplicación
app.include_router(user_router.router)
app.include_router(category_router.router)
app.include_router(task_router.router)

# una sugerencia es crear un endpoint raiz, que devuelva un mensaje:
@app.get("/")
async def read_root():

    return {"Entonces": "Mi REY "}

#: print(usuario.nombre_usuario)




