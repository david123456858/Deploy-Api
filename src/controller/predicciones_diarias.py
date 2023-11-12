
import time
from src.controller.Dolar import GetDatos,Clear,Predicciones
def get_data_prediccion():
    while True:
        data = GetDatos()
        
        # Limpiar los datos
        df = Clear(data)
        
        # Realizar predicciones
        data = Predicciones(df)
        
        # Guardar o procesar las predicciones según sea necesario
        
        # Esperar un día antes de la próxima ejecución
        time.sleep(24 * 60 * 60)  # Espera 24 horas