import talib as ta 
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf 
aapl = yf.download('AAPL', '2022-1-1','2023-03-01')

aapl['RSI'] = ta.RSI(aapl['Close'],14) 
aapl['RSI'].plot(figsize=(15,15)) 
plt.show()