from tkinter import *
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import itertools

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
    
    x = list(range(100))
    y = np.array(CLOSES)
    plt.plot(x,y, color = "black", zorder = 1)
    
    y1 = []
    y2 = []
    
    for i in CLOSES:
        if i > OPENS[CLOSES.index(i)]:
            y1.append(i) #green
            y2.append(None)
        else:
            y1.append(None)
            y2.append(i) #red
    
    y1 = np.array(y1)
    y2 = np.array(y2)
    
    plt.scatter(x, y1, s = 5, color = "green", zorder = 2)
    plt.scatter(x, y2, s = 5, color = "red", zorder = 2)

    plt.show()
    
    avg_trading_volume = int(sum(VOLUMES) / len(VOLUMES))
    

except Exception as e:
    api = "Error..."
    print(api)
    

root.mainloop()

'''

'''


