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

#from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
#from routers import user_router, category_router, task_router

#app = FastAPI()

# Montar la carpeta 'static' para servir archivos estáticos
#app.mount("/static", StaticFiles(directory="static"), name="static")

# una sugerencia es crear un endpoint raiz, que devuelva un mensaje:
#@app.get("/")
#async def read_root():
#    return {"Entonces": "Mi REY "}
#: print(usuario.nombre_usuario)


from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers import user_router, category_router, task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://127.0.0.1:8000",  # Añade aquí otros dominios si es necesario, como el de tu frontend en desarrollo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener la ruta al directorio donde se encuentra main.py
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Montar los archivos estáticos y las plantillas e
# Incluir routers de usuarios, tareas y categorias
app.include_router(user_router.router)
app.include_router(category_router.router)
app.include_router(task_router.router)

# Ruta raíz para servir el HTML principal
@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  # Asegúrate de que 'index.html' esté en tu carpeta de templates

# Si necesitas más rutas, puedes definirlas de manera similar
