��#   A P I 
-----------------

Agregue este codigo porque me tiraba error en el tipo de codigo: 
----------------
 

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
