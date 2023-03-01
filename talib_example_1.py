# All Imports
import yfinance as yf
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt

# Facebook Historial Data
fb = yf.Ticker("MSFT")
df = fb.history(start="2022-01-03")
df

plt.style.use('fivethirtyeight')
df['MA'] = ta.SMA(df['Close'],timeperiod=5)
df[['Close','MA']].plot(figsize=(8,8))
plt.show