from fastapi import FastAPI

from src.controller.Dolar import Predicciones, Clear, GetDatos
from src.controller.predicciones_diarias import get_data_prediccion
from src.controller.Acciones import GetAcciones
from src.controller.predicciones_acciones import Data, Predicciones_Acciones
from fastapi.middleware.cors import CORSMiddleware
import threading
app = FastAPI()

data_thread = threading.Thread(target=get_data_prediccion)
data_thread.daemon = True
data_thread.start()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
    
@app.get("/predicciones")
def read_root():
    data = GetDatos()
    df = Clear(data)
    return Predicciones(df)
#prueba
@app.get("/acciones/{accion}")
async def Historico_accines(accion):
    return await GetAcciones(accion)

@app.get("/acciones/predicciones/{accion}")
async def Prediccion_Accion(accion):
    df = await Data(accion)
    return Predicciones_Acciones(df)
        
if __name__ == "__Main__":
    import uvicorn
    uvicorn.run("server.api:app", reload=True)