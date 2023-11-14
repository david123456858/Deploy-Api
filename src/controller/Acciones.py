import pandas as pd
import requests

def GetAcciones(accion):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={accion}&apikey=WHBCOCJ4YJMCFL58"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        data = data.get("Time Series (Daily)")
        return data
    else:
        print("hubo un problema", reponse.status_code)
        

data = GetAcciones("IBM")   
# Limpiado_Dato(data)       