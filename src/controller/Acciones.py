import pandas as pd
import requests

def GetAcciones(accion):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={accion}&apikey=XF0U5OXCAIFK969G"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        data = data.get("Time Series (Daily)")
        print
        return data
    else:
        print("hubo un problema", reponse.status_code)
        
def Limpiado_Dato(data):
    
    time_series = data.get("Time Series (Daily)")
    df = pd.read_json(time_series)
    try:
        
        print(time_series)
    except KeyError as er:
        print(f"error: {er}")    
    

data = GetAcciones("IBM")   
# Limpiado_Dato(data)       