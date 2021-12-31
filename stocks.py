from tkinter import *
import requests
import json
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title("Stock Info")

try:
    address = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
    api_r = requests.get(address)
    data = api_r.json()
    OPENS = []
    CLOSES = []
    VOLUMES = []
    HIGHS = []
    LOWS = []

    for key in data["Time Series (5min)"]:
        OPENS.append(float(data["Time Series (5min)"][key]["1. open"]))
        HIGHS.append(float(data["Time Series (5min)"][key]["2. high"]))
        LOWS.append(float(data["Time Series (5min)"][key]["3. low"]))
        CLOSES.append(float(data["Time Series (5min)"][key]["4. close"]))
        VOLUMES.append(float(data["Time Series (5min)"][key]["5. volume"]))
    
    
        
    
    x1 = np.array(list(range(100)))
    y1 = np.array(CLOSES)
    plt.plot(x1, y1, marker = '.', color = 'red')
    
    plt.show()
    
    avg_trading_volume = int(sum(VOLUMES) / len(VOLUMES))
    

except Exception as e:
    api = "Error..."
    print(api)
    

root.mainloop()

'''
colors = []

if CLOSES > OPENS:
    colors.append('green')
else:
    colors.append('red')
'''


