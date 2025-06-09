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









