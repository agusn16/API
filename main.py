from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Modelo de datos
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

# Inicializar FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Permitir todos los origenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simula Base de datos
mensajes_db = []

# Crear un nuevo mensaje 
@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(mensaje)
    return mensaje

# Obtener mensaje por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# Muestra lista de mensajes
@app.get("/mensajes/", response_model=list[Mensaje])
def listar_mensajes():
    return mensajes_db


# Actualizar mensaje por ID
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            mensaje_actualizado.id = mensaje_id
            mensajes_db[index] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para actualizar")


