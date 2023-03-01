import talib as ta
import yfinance as yf
aapl = yf.download('AAPL', '2019-1-1','2023-03-01')
aapl['Simple MA'] = ta.SMA(aapl['Close'],14)
aapl['EMA'] = ta.EMA(aapl['Close'], timeperiod = 14)
print(aapl.tail())