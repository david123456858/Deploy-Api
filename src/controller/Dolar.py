import pandas as pd
from prophet import Prophet
import requests
import datetime 
##Cosumiendo la APi


def GetDatos():
    url = "https://www.datos.gov.co/resource/32sa-8pi3.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("hubo un problema" ,response.status_code) 
def Clear(data):
    df = pd.DataFrame(data)
    df.shape
    df.isnull().sum()
    df['fecha'] = pd.to_datetime(df['vigenciadesde']).dt.strftime("%y%m%d")
    df['ds'] = pd.to_datetime(df['fecha'], format='%y%m%d') 
    df['y'] = pd.to_numeric(df['valor'])
    df = df.iloc[:, 2:]
    return df
def Predicciones(df):
    m = Prophet()
    m.fit(df)
    future=m.make_future_dataframe(periods=3, freq='D')
    future.tail()  
    forecast=m.predict(future)
    forecast[['ds','yhat','yhat_lower', 'yhat_upper' ]]
    forecast_filtered = forecast[forecast['ds'] >= datetime.datetime(2023, 1, 1)]
    args= forecast_filtered[['ds','yhat','yhat_lower', 'yhat_upper' ]]
    data = {"datos": args.astype({'ds': 'str'}).to_dict(orient='records')}  
    return data