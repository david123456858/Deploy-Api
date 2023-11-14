import pandas as pd
import requests
import asyncio
import httpx

async def GetAcciones(accion):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={accion}&apikey=XF0U5OXCAIFK969G"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
           data = response.json()
           data = data.get("Time Series (Daily)")
           return data
        else:
               print("hubo un problema", response.status_code)
        

data = GetAcciones("IBM")   
# Limpiado_Dato(data)       