import pandas as pd
from prophet import Prophet
import requests
import datetime 
from src.controller.Acciones import GetAcciones

async def Data(accion):
    data = await GetAcciones(accion)
    if data is not None:
      df = pd.DataFrame.from_dict(data, orient= 'index')
      print(df)
    else:
     print("Data is None")
    df_prediccion = df[['4. close']]

    # Renombrar la columna para que sea más amigable
    df_prediccion = df_prediccion.rename(columns={'4. close': 'y'})

    # Convertir el índice (fechas) a formato datetime si aún no está en ese formato
    df_prediccion.index = pd.to_datetime(df_prediccion.index)   
    
    df_prediccion.index.name='ds'
    
    df_prediccion = df_prediccion.reset_index()
    
    print(df_prediccion)
    return df_prediccion

def Predicciones_Acciones(df):
    m = Prophet()
    m.fit(df)
    future=m.make_future_dataframe(periods=2, freq='D')
    future.tail()
    forecast=m.predict(future)
    forecast[['ds','yhat','yhat_lower', 'yhat_upper' ]]
    args = forecast[['ds','yhat','yhat_lower', 'yhat_upper' ]]
    data = {"predicciones": args.astype({'ds': 'str'}).to_dict(orient='records')}
    return data

