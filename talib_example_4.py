import yfinance as yf
import pandas as pd
import talib

# Download the historical data for the asset
stock = yf.Ticker("SANOFI.NS")
data = stock.history(period="max")

# Calculate the Bollinger Bands
data["upper_band"], data["middle_band"], data["lower_band"] = talib.BBANDS(data["Close"], timeperiod=20)

# Calculate the relative strength index (RSI)
data["RSI"] = talib.RSI(data["Close"], timeperiod=14)
data["RSI"].plot(figsize=(15,15)) 
plt.show()

# Calculate the MACD
data["macd"], data["macd_signal"], data["macd_hist"] = talib.MACD(data["Close"], fastperiod=12, slowperiod=26, signalperiod=9)
data[["macd", "macd_signal", "macd_hist"]].plot(figsize=(15,15)) 
plt.show()

# Calculate the stochastic oscillator
data["stochastic_k"], data["stochastic_d"] = talib.STOCH(data["High"], data["Low"], data["Close"], fastk_period=14, slowk_period=3, slowd_period=3)
data[["stochastic_k", "stochastic_d"]].plot(figsize=(15,15)) 
plt.show()