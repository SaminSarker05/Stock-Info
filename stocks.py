# make stock lookup flexible
# change dates
# add axis names 
# add own API code
# incorporate volume 
# display latests info on tkinter with BUY OR SELL

from tkinter import *
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import itertools
from matplotlib.pyplot import figure

root = Tk()
root.title("Stock Info")

ticker = "IBM"

try:
    address = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=6RO1WAKHGHC7B7VC"
    api_r = requests.get(address)
    data = api_r.json()
    OPENS = []
    CLOSES = []
    VOLUMES = []
    HIGHS = []
    LOWS = []
    DAY = ""

    for key in data["Time Series (5min)"]:
        OPENS.append(float(data["Time Series (5min)"][key]["1. open"]))
        HIGHS.append(float(data["Time Series (5min)"][key]["2. high"]))
        LOWS.append(float(data["Time Series (5min)"][key]["3. low"]))
        CLOSES.append(float(data["Time Series (5min)"][key]["4. close"]))
        VOLUMES.append(float(data["Time Series (5min)"][key]["5. volume"]))
        DAY = key[0:10]
        
    fig, axs = plt.subplots(2, 1, sharex = True)
    fig.suptitle("Price and Volume for Stock on " + DAY)
    plt.xlabel("Time (5min)")
    
    x = list(range(100))
    y = np.array(CLOSES)
    
    y1 = []
    y2 = []
    v1 = []
    v2 = []
    
    for i in CLOSES:
        if i > OPENS[CLOSES.index(i)]:
            y1.append(i) #green
            y2.append(None)
            v1.append(VOLUMES[CLOSES.index(i)])
            v2.append(0)
        else:
            y1.append(None)
            y2.append(i) #red
            v2.append(VOLUMES[CLOSES.index(i)])
            v1.append(0)
    
    y1 = np.array(y1)
    y2 = np.array(y2)
    
    axs[0].plot(x,y, color = "black", zorder = 1)
    axs[0].scatter(x, y1, s = 5, color = "green", zorder = 2)
    axs[0].scatter(x, y2, s = 5, color = "red", zorder = 2)
    axs[0].set_ylabel('Price')
    
    axs[1].bar(x, v1, color = "green")
    axs[1].bar(x, v2, color = "red")
    axs[1].set_ylabel('Volume')
    
    plt.show()
    
    avg_trading_volume = int(sum(VOLUMES) / len(VOLUMES))
    
    
except Exception as e:
    api = "Error..."
    print(api)
    
root.mainloop()
